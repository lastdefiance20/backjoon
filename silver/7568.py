import sys

N = int(sys.stdin.readline())

bulk_table = []
index_table = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    bulk_table.append([x, y])
    index_table.append(1)
    
while sum(index_table):
    for idx in len(bulk_table):
        if index_table[idx] == 1:
            if bulk_table[idx][x] > 