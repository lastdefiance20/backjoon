#union find 문제

import sys

N, M = map(int, sys.stdin.readline().split())

def add_connection(node1, node2, parent):
    node1 = find_parent(node1, parent)
    node2 = find_parent(node2, parent)
    if node1 != node2:
        parent[node2] = node1

def find_parent(node, parent):
    if node == parent[node]:
        return node
    else:
        return find_parent(parent[node], parent)

def same_node(node1, node2, parent):
    if find_parent(node1, parent) == find_parent(node2, parent):
        return True
    else:
        return False

parent = [i for i in range(N+1)]

know_truth = list(map(int, sys.stdin.readline().split()))
truth_head = 0

for i in range(know_truth[0]):
    if truth_head == 0:
        truth_head = know_truth[i+1]
    else:
        add_connection(truth_head, know_truth[i+1], parent)

party_list = []
for _ in range(M):
    party = list(map(int, sys.stdin.readline().split()))
    len_party = party[0]
    party_head = 0
    if len_party > 1:
        for i in range(len_party):
            if party_head == 0:
                party_head = party[i+1]
            else:
                add_connection(party_head, party[i+1], parent)
    party_list.append(party)

know_dic = {}
know_dic[truth_head] = 1
for i in range(1, N+1):
    if same_node(truth_head, i, parent):
        know_dic[i] = 1

result = 0
for i in range(M):
    can_lie = True
    for j in range(party_list[i][0]):
        if party_list[i][j+1] in know_dic:
            can_lie = False
            break
    if can_lie:
        result+=1
print(result)