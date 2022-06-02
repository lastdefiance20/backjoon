import sys
import copy

N, M, V = map(int, sys.stdin.readline().split())

graph_list = [[] for x in range(1001)]

for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())

    graph_list[node1].append(node2)
    graph_list[node2].append(node1)

graph_list_tmp = copy.deepcopy(graph_list)

###### DFS ######
visited_node = [V]

visit_needed = graph_list[V]
visit_needed.sort(reverse = True)

graph_list[V] = []

while visit_needed:
    node = visit_needed.pop()

    if len(graph_list[node]) == 0:
        continue

    graph_list[node].sort(reverse = True)

    for tmp in graph_list[node]:
        visit_needed.append(tmp)

    graph_list[node] = []
    visited_node.append(node)

visited_node = map(str, visited_node)
print(" ".join(visited_node))

graph_list = graph_list_tmp

###### BFS ######
visited_node = [V]

visit_needed = graph_list[V]
visit_needed.sort()

graph_list[V] = []

while visit_needed:
    node = visit_needed.pop(0)

    if len(graph_list[node]) == 0:
        continue

    graph_list[node].sort()

    for tmp in graph_list[node]:
        visit_needed.append(tmp)

    graph_list[node] = []
    visited_node.append(node)

visited_node = map(str, visited_node)
print(" ".join(visited_node))