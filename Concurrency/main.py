from criticalSection import CriticalSection
from boundedBuffer import BoundedBuffer
import threading


def test_critical_section():
    cs = CriticalSection()

    threads = []

    for i in range(10):
        t = threading.Thread(target=cs.critical_section, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def test_bounded_buffer():
    bb = BoundedBuffer(5)

    producer_threads = threading.Thread(
        target=lambda: [bb.producer(i) for i in range(10)]
    )
    consumer_threads = threading.Thread(
        target=lambda: [bb.consumer() for _ in range(10)]
    )

    producer_threads.start()
    consumer_threads.start()

    producer_threads.join()
    consumer_threads.join()


if __name__ == "__main__":
    print("Testing critical section")
    # test_critical_section()
    print("Testing bounded buffer")
    test_bounded_buffer()
