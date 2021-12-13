import sys

n, k = map(int, sys.stdin.readline().split())

circle = [x for x in range(1, n+1)]
index = 0

print("<", end = "")
for i in range(n):
    index += k-1
    index = index%len(circle)
    if(len(circle) == 1):
        print(circle.pop(index), end = ">")
    else:
        print(circle.pop(index), end = ", ")