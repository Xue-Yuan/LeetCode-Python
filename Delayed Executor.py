import asyncio
import collections
import heapq
from typing import Callable, Tuple, Dict, Any, Optional

Task = collections.namedtuple(
    "Task", ["start_time", "task_id", "func", "args", "kwargs"])


class AsyncTaskExecutor:

    def __init__(self):
        self.tasks = []  # Heap queue to manage tasks
        # Lock for thread-safe operations on the heap
        self.tasks_lock = asyncio.Lock()
        # Condition variable for efficient scheduling
        self.condition = asyncio.Condition(self.tasks_lock)
        # To maintain unique task IDs for cancellation
        self.task_counter_lock = asyncio.Lock()
        self.task_counter = 0
        self.loop = asyncio.get_event_loop()

    async def _new_task_id(self):
        async with self.task_counter_lock:
            self.task_counter += 1
            return self.task_counter

    async def _schedule_next_locked(self) -> Optional[float]:
        assert self.tasks_lock.locked()
        while self.tasks:
            task = self.tasks[0]
            now = self.loop.time()
            if now >= task.start_time:
                task = heapq.heappop(self.tasks)
                asyncio.create_task(task.func(*task.args, **task.kwargs))
            else:
                return task.start_time - now
        return None

    async def _loop(self):
        while True:
            async with self.condition:
                wait_time = await self._schedule_next_locked()
                if wait_time is None:
                    # Wait until notified of a new task
                    await self.condition.wait()
                else:
                    try:
                        await asyncio.wait_for(self.condition.wait(),
                                               timeout=wait_time)
                    except TimeoutError:
                        print(f'wait_time={wait_time} has passed!')

    async def schedule_task(self, timestamp: float, func: Callable, *args: Any,
                            **kwargs: Any) -> int:
        """Schedule a task to be run at a specific timestamp in the future."""
        async with self.condition:
            task_id = await self._new_task_id()
            heapq.heappush(self.tasks,
                           Task(timestamp, task_id, func, args, kwargs))
            self.condition.notify()
        return task_id

    async def cancel_task(self, task_id: int) -> bool:
        """Cancel a scheduled task if it hasn't started."""
        async with self.condition:
            for i, task in enumerate(self.tasks):
                if task.task_id == task_id:
                    self.tasks.pop(i)
                    heapq.heapify(self.tasks)
                    self.condition.notify()
                    return True
        return False

    def start(self):
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

    await timer(end=30)


if __name__ == '__main__':
    asyncio.run(main())
