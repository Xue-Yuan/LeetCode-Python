import asyncio
import collections
import heapq
from typing import Callable, Any, Optional

Task = collections.namedtuple(
    "Task", ["start_time", "task_id", "func", "args", "kwargs"])


class AsyncTaskExecutor:
    """Basic ideas:
    1. Start an event loop, which keeps polling the heap for the task that's
    scheduled in the nearest future. If no task, wait for new tasks being
    added.
    2. Add new tasks into a min heap based on the task start time. If a task
    can be scheduled, pop it out of the heap and run it.
    3. To cancel a task, iterate through the heap, match the task id, and pop
    it out of the heap.
    """

    def __init__(self):
        # Heap queue to manage tasks
        self.tasks = []
        self.lock = asyncio.Lock()
        # Condition variable for efficient scheduling
        self.condition = asyncio.Condition(self.lock)
        # To maintain unique task IDs for cancellation
        self.task_counter = 0
        self.loop = asyncio.get_event_loop()

    def _new_task_id(self):
        self.task_counter += 1
        return self.task_counter

    async def _schedule_next_locked(self) -> Optional[float]:
        assert self.lock.locked()
        while self.tasks:
            task = self.tasks[0]
            now = self.loop.time()
            if task.start_time <= now:
                heapq.heappop(self.tasks)
                asyncio.create_task(task.func(*task.args, **task.kwargs))
            else:
                return now - task.start_time
        return None

    async def _loop(self):
        while True:
            async with self.condition:
                wait_time = await self._schedule_next_locked()
                if wait_time is None:
                    await self.condition.wait()
                else:
                    try:
                        await asyncio.wait_for(self.condition.wait(),
                                               timeout=wait_time)
                    except TimeoutError:
                        pass

    async def schedule_task(self, timestamp: float, func: Callable, *args: Any,
                            **kwargs: Any) -> int:
        async with self.condition:
            task = Task(timestamp, self._new_task_id(), func, args, kwargs)
            heapq.heappush(self.tasks, task)
            self.condition.notify()
        return task.task_id

    async def cancel_task(self, task_id: int) -> bool:
        """Cancel a scheduled task if it hasn't started."""
        async with self.lock:
            for i, task in enumerate(self.tasks):
                if task.task_id != task_id:
                    continue
                self.tasks[i] = self.tasks[-1]
                self.tasks.pop()
                heapq.heapify(self.tasks)
                return True
            return False

    def start(self) -> None:
        asyncio.create_task(self._loop())


async def example_task(message: str):
    print(f"Task executed: {message}")


async def timer(end: int):
    cnt = 0
    while True:
        cnt += 1
        print(f'time: {cnt} seconds')
        await asyncio.sleep(1)
        if cnt >= end:
            break
    print(f'{end} seconds passed. End.')


async def main():
    executor = AsyncTaskExecutor()
    executor.start()

    # Schedule a task to run 5 seconds from now
    task_id = await executor.schedule_task(asyncio.get_event_loop().time() + 5,
                                           example_task, "Hello World second!")
    print(f"Scheduled a task (id={task_id}) in 5 seconds")

    task_id = await executor.schedule_task(asyncio.get_event_loop().time() + 8,
                                           example_task, "Hello World third!")
    print(f"Scheduled a task (id={task_id}) in 8 seconds")

    task_id = await executor.schedule_task(asyncio.get_event_loop().time() + 3,
                                           example_task, "Hello World first!")
    print(f"Scheduled a task (id={task_id}) in 3 seconds")

    # Cancel the task before it runs
    cancelled = await executor.cancel_task(task_id)
    print(f"task_id={task_id} cancelled={cancelled}")

    await timer(end=15)


if __name__ == '__main__':
    asyncio.run(main())
