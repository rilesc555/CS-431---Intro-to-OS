from semaphore import Semaphore

class BoundedBuffer:
    def __init__(self, size):
        self.semaphore_empty = Semaphore(size)
        self.semaphore_full = Semaphore(0)
        self.buffer = [None] * size

    def producer(self, item):
        self.semaphore_empty.P()
        self.buffer.append(item)
        print(f'Produced {item}')
        self.semaphore_full.V()

    def consumer(self):
        # Wait until there is an item to consume
        self.semaphore_full.P()

        # Consume the item
        item = self.buffer.pop(0)
        print(f'Consumed {item}')

        # Signal that there is an empty slot in the buffer
        self.semaphore_empty.V()