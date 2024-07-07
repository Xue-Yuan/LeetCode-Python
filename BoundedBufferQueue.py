import threading
import collections
import time
import random


class BoundedBufferQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = collections.deque()
        self.mutex = threading.Lock()
        self.not_full = threading.Condition(self.mutex)
        self.not_empty = threading.Condition(self.mutex)

    def put(self, item):
        with self.not_full:
            while len(self.queue) >= self.capacity:
                self.not_full.wait()
            self.queue.append(item)
            self.not_empty.notify()

    def get(self):
        with self.not_empty:
            while len(self.queue) == 0:
                self.not_empty.wait()
            item = self.queue.popleft()
            self.not_full.notify()
            return item


# Example usage
if __name__ == "__main__":

    buffer = BoundedBufferQueue(10)

    def producer():
        for i in range(20):
            buffer.put(i)
            print(f'Produced {i}')
            time.sleep(random.uniform(0.1, 0.5))

    def consumer():
        for _ in range(20):
            item = buffer.get()
            print(f'Consumed {item}')
            time.sleep(random.uniform(0.1, 0.5))

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
