import sys

n = int(sys.stdin.readline())

bulk_table = []
index_table = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    bulk_table.append([x, y])
    index_table.append(n)

for source_idx in range(len(bulk_table)):
    for compare_idx in range(len(bulk_table)):
        if source_idx != compare_idx:
            if(bulk_table[source_idx][0] >= bulk_table[compare_idx][0]):
                index_table[source_idx] -= 1
            elif(bulk_table[source_idx][1] >= bulk_table[compare_idx][1]):
                index_table[source_idx] -= 1

print(" ".join(map(str, index_table)))