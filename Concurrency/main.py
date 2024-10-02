from criticalSection import CriticalSection
import threading

cs = CriticalSection()

threads = []

for i in range(10):
    t = threading.Thread(target=cs.critical_section, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()