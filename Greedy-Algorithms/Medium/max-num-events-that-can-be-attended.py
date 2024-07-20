import heapq

def maxEvents(N, start, end):
    events = sorted(zip(start, end))
    min_heap = []
    i, event_count, day = 0, 0, 0

    while i < N or min_heap:
        if not min_heap:
            day = events[i][0]
        
        while i < N and events[i][0] <= day:
            heapq.heappush(min_heap, events[i][1])
            i += 1

        if min_heap:
            heapq.heappop(min_heap)
            event_count += 1
            day += 1

        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)
    
    return event_count

# Example usage:
N1 = 3
start1 = [1, 2, 1]
end1 = [1, 2, 2]
print(maxEvents(N1, start1, end1))  # Output: 2

N2 = 3
start2 = [1, 2, 3]
end2 = [2, 3, 4]
print(maxEvents(N2, start2, end2))  # Output: 3
