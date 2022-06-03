import sys
from collections import deque

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

adj_list = [[] for x in range(N+1)]

for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

def BFS(adj_list):
    queue = deque()
    queue.append(1)
    
    virus = 0

    while queue:
        node = queue.popleft()
        if adj_list[node] != []:
            virus += 1

            for tmp in adj_list[node]:
                queue.append(tmp)
            
            adj_list[node] = []
    
    return virus - 1

print(BFS(adj_list))
