import re
from typing import List
import heapq
import numpy as np


def SJF(processes: List[List]):
    """
    processes: [[process, arrival_time, burst_time]]
    """

    # Variables to keep track of current time, turnaround times and completion times
    current_time = 0
    turnaround_times = {}
    completion_times = {}

    # Ready queue to store processes that are ready to be executed. It is a min heap based on burst time, then arrival time, then process id
    ready_queue = []

    def execute_process():
        """inner function to get the shortest job from ready queue, simulate its execution,
        update current time and store completion and turnaround times.
        If ready queue is empty, just increments current time and returns.
        """
        nonlocal current_time
        if not ready_queue:
            current_time += 1
            return
        burst, arrival, process_id = heapq.heappop(ready_queue)
        print(f"Process {process_id} started at {current_time}")
        current_time += burst
        print(f"Process {process_id} finished at {current_time}")
        completion_times[process_id] = current_time
        turnaround_times[process_id] = current_time - arrival

    # get all processes that have arrived by current time and add them to ready queue, then execute the process with shortest burst time
    while processes:
        for i in range(len(processes) - 1, -1, -1):
            (process_id, arrival_time, burst_time) = processes[i]
            if arrival_time <= current_time:
                heapq.heappush(ready_queue, (burst_time, arrival_time, process_id))
                del processes[i]
        execute_process()

    # execute remaining processes in ready queue
    while ready_queue:
        execute_process()

    return turnaround_times, completion_times

def SRT(origprocesses: List[List]):
    '''
    pre-emptive version of SJF
    processes: [[process, arrival_time, burst_time]]
    '''

    # Variables to keep track of current time, turnaround times and completion times
    processes = origprocesses.copy()
    current_time = 0
    turnaround_times = {}
    completion_times = {}

    # Ready queue to store processes that are ready to be executed. It is a min heap based on burst time, then arrival time, then process id
    ready_queue = []

    def execute_process():
        """inner function to get the shortest job from ready queue, simulate its execution,
        update current time and store completion and turnaround times.
        If ready queue is empty, just increments current time and returns.
        """
        nonlocal current_time
        if not ready_queue:
            current_time += 1
            return
        burst, arrival, process_id = heapq.heappop(ready_queue)
        if process_id not in completion_times:
            print(f"Process {process_id} started at {current_time}")
            completion_times[process_id] = current_time
        else:
            print(f"Process {process_id} resumed at {current_time}")
        current_time += 1
        burst -= 1
        completion_times[process_id] += 1
        if burst == 0:
            print(f"Process {process_id} finished at {current_time}")
            turnaround_times[process_id] = current_time - arrival
        else:
            heapq.heappush(ready_queue, (burst, arrival, process_id))

    # get all processes that have arrived by current time and add them to ready queue, then execute the process with shortest burst time
    while processes:
        for i in range(len(processes) - 1, -1, -1):
            (process_id, arrival_time, burst_time) = processes[i]
            if arrival_time <= current_time:
                heapq.heappush(ready_queue, (burst_time, arrival_time, process_id))
                del processes[i]
        execute_process()

    # execute remaining processes in ready queue
    while ready_queue:
        execute_process()

    return turnaround_times, completion_times

sjf_processes = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5], [5, 8, 2]]
srt_processes = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5], [5, 8, 2]]

turnaround_times, completion_times = SJF(sjf_processes)

print("SJF Turnaround Times:")
print(turnaround_times)
print("SJF Completion Times:")
print(completion_times)

print("SJF Average Turnaround Time:", np.mean(list(turnaround_times.values())))

turnaround_times, completion_times = SRT(srt_processes)

print("SRT Turnaround Times:")
print(turnaround_times)
print("SRT Completion Times:")
print(completion_times)

print("SRT Average Turnaround Time:", np.mean(list(turnaround_times.values())))
