import threading


class Semaphore:
    def __init__(self, initial):
        # Create a condition variable to associate with a lock
        # This is used to synchronize threads
        self.lock = threading.Condition(threading.Lock())

        self.value = initial

    def P(self):
        # Acquire the lock if available
        with self.lock:
            while self.value <= 0:
                self.lock.wait()
            self.value -= 1

    def V(self):
        with self.lock:
            self.value += 1
            self.lock.notify()
