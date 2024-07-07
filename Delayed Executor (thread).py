import threading
import collections
import heapq
from typing import Callable, Any, Optional
import time

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
        self.lock = threading.Lock()
        # Condition variable for efficient scheduling
        self.condition = threading.Condition(self.lock)
        # To maintain unique task IDs for cancellation
        self.task_counter_lock = threading.Lock()
        self.task_counter = 0

    def _new_task_id(self):
        with self.task_counter_lock:
            self.task_counter += 1
            return self.task_counter

    def _schedule_next_locked(self) -> Optional[float]:
        assert self.lock.locked()
        while self.tasks:
            task = self.tasks[0]
            now = time.time()
            if task.start_time <= now:
                heapq.heappop(self.tasks)
                threading.Thread(target=task.func,
                                 args=task.args,
                                 kwargs=task.kwargs).start()
            else:
                return task.start_time - now
        return None

    def _loop(self):
        while True:
            print('loop')
            with self.condition:
                wait_time = self._schedule_next_locked()
                if wait_time is None:
                    self.condition.wait()
                else:
                    self.condition.wait(timeout=wait_time)

    def schedule_task(self, timestamp: float, func: Callable, *args: Any,
                      **kwargs: Any) -> int:
        with self.condition:
            task = Task(timestamp, self._new_task_id(), func, args, kwargs)
            heapq.heappush(self.tasks, task)
            self.condition.notify()
        return task.task_id

    def cancel_task(self, task_id: int) -> bool:
        """Cancel a scheduled task if it hasn't started."""
        with self.lock:
            for i, task in enumerate(self.tasks):
                if task.task_id != task_id:
                    continue
                self.tasks[i] = self.tasks[-1]
                self.tasks.pop()
                heapq.heapify(self.tasks)
                return True
            return False

    def start(self) -> None:
        threading.Thread(target=self._loop).start()


def example_task(message: str):
    print(f"Task executed: {message}")


def timer(end: int):
    cnt = 0
    while True:
        cnt += 1
        print(f'time: {cnt} seconds')
        time.sleep(1)
        if cnt >= end:
            break
    print(f'{end} seconds passed. End.')


def main():
    t = threading.Thread(target=timer, args=(15, ))
    t.start()

    executor = AsyncTaskExecutor()
    executor.start()

    # Schedule a task to run 5 seconds from now
    task_id = executor.schedule_task(time.time() + 5, example_task,
                                     "Hello World second!")
    print(f"Scheduled a task (id={task_id}) in 5 seconds")

    task_id = executor.schedule_task(time.time() + 8, example_task,
                                     "Hello World third!")
    print(f"Scheduled a task (id={task_id}) in 8 seconds")

    task_id = executor.schedule_task(time.time() + 3, example_task,
                                     "Hello World first!")
    print(f"Scheduled a task (id={task_id}) in 3 seconds")

    # Cancel the task before it runs
    cancelled = executor.cancel_task(task_id)
    print(f"task_id={task_id} cancelled={cancelled}")

    t.join()


if __name__ == '__main__':
    main()
