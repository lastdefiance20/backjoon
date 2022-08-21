import heapq
import sys

N = int(sys.stdin.readline())
heap = []
len_heap = 0

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len_heap == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            len_heap -= 1

    else:
        if x < 0:
            heapq.heappush(heap, (-x, x))
            len_heap += 1
        else:
            heapq.heappush(heap, (x, x))
            len_heap += 1