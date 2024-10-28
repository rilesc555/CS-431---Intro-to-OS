from collections import deque

ref_string = [0, 1, 4, 0, 2, 3, 0, 1, 0, 2, 3, 4, 2, 3]
frame_size = 4
frames = [0, 1, 2, 3]


def fifo(pages, frame_size, frames):
    frame_queue = frames
    page_faults = 0
    for page in pages:
        if page not in frame_queue:
            page_faults += 1
            print(f"Page {page} caused a page fault")

            if len(frame_queue) < frame_size:
                frame_queue.append(page)
            else:
                frame_queue.pop(0)
                frame_queue.append(page)
    return page_faults

def lru(pages, frame_size, frames):
    frame_queue = deque(pages)
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

print(f"Page faults: {fifo(ref_string, frame_size, frames)}")

print(f"Page faults: {lru(ref_string, frame_size, frames)}")

