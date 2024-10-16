import time
import numpy as np


class Bankers:
    """implement Bankers algorithm"""

    def __init__(
        self, curr_alloc: np.ndarray, max_ask: np.ndarray, available: np.array
    ):
        self.allocation = curr_alloc
        self.max = max_ask
        self.available = available
        self.need = max_ask - curr_alloc
        self.num_processes = len(curr_alloc)
        self.num_resources = len(available)
        self.running = np.ones(self.num_processes)

    def is_safe(self) -> None:
        sequence = []
        while np.any(self.running):
            allocated = False
            for p in range(self.num_processes):
                if self.running[p]:
                    if all(
                        i >= 0
                        for i in self.available - (self.max[p] - self.allocation[p])
                    ):
                        allocated = True
                        print(f"Process {p} is running")
                        time.sleep(0.5)
                        sequence.append(p)
                        self.running[p] = 0
                        self.available += self.allocation[p]
            if not allocated:
                print("Unsafe - no possible sequences")
                return
        print(f"Safe sequence: ", end="")
        for p in sequence:
            print(f"{p} ", end="")
        print()
        return


def main():
    Allocation = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]], int)
    Max = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]], int)
    Available = np.array([3, 3, 2], int)

    banker = Bankers(Allocation, Max, Available)

    banker.is_safe()


if __name__ == "__main__":
    main()
