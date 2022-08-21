# stack 대신 우선순위 큐

import sys
import heapq

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
bigger_list = [-1 for _ in range(N)]
min_heap = []
heap_len = 0

for idx in range(0, N):
    for _ in range(heap_len):
        if min_heap[0][0] < num_list[idx]:
            bigger_list[heapq.heappop(min_heap)[1]] = num_list[idx]
            heap_len -= 1
        else:
            break

    heapq.heappush(min_heap, (num_list[idx], idx))
    heap_len += 1

bigger_list = [str(i) for i in bigger_list]
print(" ".join(bigger_list))