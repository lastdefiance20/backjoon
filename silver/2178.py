import sys
from collections import deque

def BFS(N, M, maze):
    queue = deque()
    queue.append([0,0,1])

    while queue:
        x, y, val = queue.popleft()

        if x == M-1 and y == N-1:
            return val
            
        if maze[y][x] == 0:
            continue

        x_inv = (x-1) >= 0
        x_inf = (x+1) < M
        y_inv = (y-1) >= 0
        y_inf = (y+1) < N

        if x_inv:
            if maze[y][x-1] == 1:
                queue.append([x-1, y, val+1])
        
        if x_inf:
            if maze[y][x+1] == 1:
                queue.append([x+1, y, val+1])

        if y_inv:
            if maze[y-1][x] == 1:
                queue.append([x, y-1, val+1])

        if y_inf:
            if maze[y+1][x] == 1:
                queue.append([x, y+1, val+1])

        maze[y][x] = 0

N, M = map(int, sys.stdin.readline().split())

maze = []
for i in range(N):
    tmp = []
    for val in sys.stdin.readline().rstrip():
        tmp.append(int(val))
    maze.append(tmp)

print(BFS(N, M, maze))
