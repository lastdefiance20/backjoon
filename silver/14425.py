import sys

N, M = map(int, sys.stdin.readline().split())

name_dic = {}

for _ in range(N):
    name_dic[sys.stdin.readline()] = 1

result = 0
for _ in range(M):
    if sys.stdin.readline() in name_dic:
        result += 1

print(result)