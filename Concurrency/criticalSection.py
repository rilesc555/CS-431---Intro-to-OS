import time
from semaphore import Semaphore
class CriticalSection:
    def __init__(self):
        # Create a semaphore with a value of 1 to ensure mutual exclusion
        self.semaphore = Semaphore(1)
    
    def critical_section(self, p):
        self.semaphore.P()
        print(f"Process {p} entered the critical section")
        print(f"Process {p} is running the critical section")
        time.sleep(3)
        print(f"Process {p} exited the critical section")
        self.semaphore.V()