import sys

n, m = map(int, sys.stdin.readline().split())
result = (n-1)+n*(m-1)

print(result)