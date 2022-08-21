import sys
from collections import deque

def check_boundary(x, y, w, h):
    if x < 0 or x >= w:
        return False
    elif y < 0 or y >= h:
        return False
    else:
        return True

def BFS(x, y, M, N, array):
    deq = deque()
    array[y][x] = 0
    deq.append((x, y))

    while len(deq):
        x, y = deq.popleft()

        for x1, y1 in [(x, y+1), (x+1, y), (x-1, y), (x, y-1)]:
            if check_boundary(x1, y1, M, N):
                if array[y1][x1] == 1:
                    array[y1][x1] = 0
                    deq.append((x1, y1))

T = int(sys.stdin.readline())

for _ in range(T):

    M, N, K = map(int, sys.stdin.readline().split())

    # initialize ground
    ground_list = []
    for _ in range(N):
        ground_list.append([0 for _ in range(M)])

    # add cabbage
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        ground_list[y][x] = 1

    result = 0
    for y in range(N):
        for x in range(M):
            if ground_list[y][x] == 1:
                result+=1
                BFS(x, y, M, N, ground_list)

    print(result)