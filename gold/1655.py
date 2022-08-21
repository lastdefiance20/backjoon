import heapq
import sys

N = int(sys.stdin.readline())

left_heap = [] # 최대값 heap
right_heap = [] # 최소값 heap
median = [int(sys.stdin.readline())]
print(median[0])

for _ in range(N-1):
    x = int(sys.stdin.readline())

    if len(median) == 1:
        if median[0] < x:
            heapq.heappush(right_heap, (x, x))
            median.append(heapq.heappop(right_heap)[1])
            median.sort()
            print(median[0])
        else:
            heapq.heappush(left_heap, (-x, x))
            median.append(heapq.heappop(left_heap)[1])
            median.sort()
            print(median[0])

    else:
        if median[1] < x:
            heapq.heappush(right_heap, (x, x))
            heapq.heappush(left_heap, (-median[0], median[0]))
            median = [median[1]]
            print(median[0])

        elif median[0] > x:
            heapq.heappush(left_heap, (-x, x))
            heapq.heappush(right_heap, (median[1], median[1]))
            median = [median[0]]
            print(median[0])

        else:
            heapq.heappush(right_heap, (median[1], median[1]))
            heapq.heappush(left_heap, (-median[0], median[0]))
            median = [x]
            print(median[0])