import sys
from collections import deque

def BFS(x, y, N, area):
    queue = deque()
    queue.append([x,y])

    val = 0

    while queue:
        x, y = queue.popleft()
            
        if area[y][x] == 0:
            continue

        x_inv = (x-1) >= 0
        x_inf = (x+1) < N
        y_inv = (y-1) >= 0
        y_inf = (y+1) < N

        if x_inv:
            if area[y][x-1] == 1:
                queue.append([x-1, y])
        
        if x_inf:
            if area[y][x+1] == 1:
                queue.append([x+1, y])

        if y_inv:
            if area[y-1][x] == 1:
                queue.append([x, y-1])

        if y_inf:
            if area[y+1][x] == 1:
                queue.append([x, y+1])

        area[y][x] = 0
        val += 1

    return val

N = int(sys.stdin.readline())

area = []
for i in range(N):
    tmp = []
    for val in sys.stdin.readline().rstrip():
        tmp.append(int(val))
    area.append(tmp)

house = []

for y in range(N):
    for x in range(N):
        if area[y][x] == 1:
            house.append(BFS(x, y, N, area))

house.sort()

print(len(house))
for num in house:
    print(num)