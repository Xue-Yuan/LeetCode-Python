"""A simple reader-writer lock in Python
"""

import threading


class RWLock:
    def __init__(self):
        self.readers = 0
        self.writers = 0
        self.mutex = threading.Lock()
        self.readers_cond = threading.Condition(self.mutex)
        self.writers_cond = threading.Condition(self.mutex)

    def r_acquire(self):
        self.mutex.acquire()
        while self.writers:
            self.readers_cond.wait()
        self.readers += 1
        self.mutex.release()

    def r_release(self):
        self.mutex.acquire()
        self.readers -= 1
        if not self.readers:
            self.writers_cond.notify()
        self.mutex.release()

    def w_acquire(self):
        self.mutex.acquire()
        while self.readers or self.writers:
            self.writers_cond.wait()
        self.writers += 1
        self.mutex.release()

    def w_release(self):
        self.mutex.acquire()
        self.writers -= 1
        self.readers_cond.notifyAll()
        self.writers_cond.notify()
        self.mutex.release()
