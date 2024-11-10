from collections import deque
from turtle import up

import numpy as np

ref_string = [0, 1, 4, 0, 2, 3, 0, 1, 0, 2, 3, 4, 2, 3]
frame_size = 4
initial_frames = [0, 1, 2, 3]


def fifo(ref_string, frame_size):
    """
    Takes in a reference string and frame size and simulates the FIFO page replacement algorithm
    ref_string: list of integers representing sequence of page references
    frame_size: integer representing the number of frames

    """
    print("FIFO algorithm")
    frame_queue = deque(initial_frames.copy())
    page_faults = 0
    for page in ref_string:
        if page not in frame_queue:
            page_faults += 1
            print(f"Page {page} caused a page fault")

            if len(frame_queue) < frame_size:
                frame_queue.append(page)
            else:
                frame_queue.popleft()
                frame_queue.append(page)
        print(f"Frames (first to last reference): {frame_queue}")
    print("End of FIFO algorithm")
    print(f"Page faults: {page_faults}")


def lru(pages, frame_size):
    print("LRU algorithm")
    frame_queue = deque(initial_frames.copy())
    page_faults = 0
    for page in pages:
        # if ref string already in frames, remove it and append it to the end
        if page in frame_queue:
            frame_queue.remove(page)
            frame_queue.append(page)
        else:
            page_faults += 1
            print(f"Page {page} caused a page fault")
            if len(frame_queue) < frame_size:
                frame_queue.append(page)
            else:
                frame_queue.popleft()
                frame_queue.append(page)

    print("End of LRU algorithm")
    print(f"Page faults: {page_faults}")


def optimal(pages, frame_size):
    print("Optimal algorithm")

    def update_time_to_next_ref():
        for page in frames:
            if page in pages[pos + 1 :]:
                time_to_next_ref[page] = pages.index(page, pos + 1)
            else:
                time_to_next_ref[page] = np.inf

    # initialize dict to store next reference of each page
    time_to_next_ref = {}
    pos = 0
    for i, page in enumerate(pages):
        if page not in time_to_next_ref:
            time_to_next_ref[page] = i
    frames = []
    page_faults = 0

    for page in pages:
        if page not in frames:
            page_faults += 1
            print(f"Page {page} caused a page fault")
            if len(frames) < frame_size:
                frames.append(page)
                print(f"Page {page} added to frames")
            else:
                # find the page that will not be used for the longest time
                page_to_remove = max(frames, key=lambda x: time_to_next_ref[x])
                frames.remove(page_to_remove)
                frames.append(page)
                print(f"Page {page_to_remove} removed from frames")
        else:
            print(f"Page {page} already in frames")

        update_time_to_next_ref()
        pos += 1
        print(f"Frames: {frames}")
    print("End of Optimal algorithm. Page faults: ", page_faults)


def main():
    fifo(ref_string, frame_size)
    print()
    lru(ref_string, frame_size)
    print()
    optimal(ref_string, frame_size)


if __name__ == "__main__":
    main()
