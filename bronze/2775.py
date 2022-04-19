import sys

findpeoplelist = [[0 for y in range(15)] for x in range(15)]

def findpeople(k, n):
    if k == 0:
        return n
    else:
        if findpeoplelist[k][n] != 0:
            return findpeoplelist[k][n]
        total = 0
        for i in range(1, n+1):
            total += findpeople(k-1, i)
        findpeoplelist[k][n] = total
        return findpeoplelist[k][n]

T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(findpeople(k, n))