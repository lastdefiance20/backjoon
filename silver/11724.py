import sys

N, M = map(int, sys.stdin.readline().split())

node_list = [[] for x in range(N+1)]
queue = [1]
reached_queue = [n for n in range(1, N+1)]
component = 0

#bfs
for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    node_list[node1].append(node2)
    node_list[node2].append(node1)

while queue:
    while queue:
        node = queue.pop()
        
        if node_list[node] == 0:
            continue

        for tmp in node_list[node]:
            queue.append(tmp)

        node_list[node] = 0

    component += 1

    while reached_queue:
        node = reached_queue.pop()
        if node_list[node] != 0:
            queue.append(node)
            break

print(component)