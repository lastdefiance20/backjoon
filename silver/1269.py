import sys

A, B = map(int, sys.stdin.readline().split())

set_a = set(list(map(int, sys.stdin.readline().split())))
set_b = set(list(map(int, sys.stdin.readline().split())))

print(len(set_a-set_b)+len(set_b-set_a))