import sys

n = sys.stdin.readline().rstrip()

num_list = [0 for x in range(10)]

for x in n:
    num_list[int(x)] += 1

for i in range(9, -1, -1):
    for idx in range(num_list[i]):
        print(i, end = "")