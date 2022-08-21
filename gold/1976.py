# 유니온 파인드 관련 문제

import sys
def invint(x):
    return(int(x)-1)

# 노드를 합치는 union 연산
def add(node1, node2, union_array):
    node1 = find(node1, union_array)
    node2 = find(node2, union_array)
    if node1 != node2:
        union_array[node1] = node2

# 루트 노드를 찾는 find 연산
def find(node, union_array):
    if union_array[node] != node:
        return find(union_array[node], union_array)
    else:
        return node

def is_same_graph(node1, node2, union_array):
    if find(node1, union_array) == find(node2, union_array):
        return True
    else:
        return False

def check_trip(trip, union_array):
    for i in range(0, M-1):
        if not is_same_graph(trip[i], trip[i+1], union_array):
            print("NO")
            return
    print("YES")
    return

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

plan = []
for _ in range(N):
    plan.append(list(map(int, sys.stdin.readline().split())))

union_array = [x for x in range(N)]

for y in range(0, N):
    for x in range(1+y, N):
        if plan[y][x] == 1:
            add(x, y, union_array)

trip = list(map(invint, sys.stdin.readline().split()))
check_trip(trip, union_array)