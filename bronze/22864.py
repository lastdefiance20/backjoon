import sys

a, b, c, m = map(int, sys.stdin.readline().split())

work = 0
fatigue = 0

for i in range(24):
    if fatigue + a > m:
        fatigue -= c
        if fatigue < 0:
            fatigue = 0

    else:
        work += b
        fatigue += a

print(work)