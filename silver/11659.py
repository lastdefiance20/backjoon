import sys

N, M = map(int, sys.stdin.readline().split())

number_list = list(map(int, sys.stdin.readline().split()))

sum_list = []
tmp = 0

for num in number_list:
    tmp += num
    sum_list.append(tmp)

for i in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_list[j-1] - sum_list[i-1] + number_list[i-1])