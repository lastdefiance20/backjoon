import sys

n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    many = ["empty", 0]
    for i in range(m):
        a, b = sys.stdin.readline().split()
        a.rstrip()
        b = int(b)

        if b > many[1]:
            many[1] = b
            many[0] = a
    print(many[0])