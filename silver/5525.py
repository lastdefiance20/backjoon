import sys

N = int(sys.stdin.readline())

N = N*2-1

M = int(sys.stdin.readline())

S = sys.stdin.readline().rstrip()

streak = 0

result = 0

for x in S:
    if streak %2 == 0 and x == "I":
        streak += 1
    elif streak %2 == 1 and x == "O":
        streak += 1
    else:
        if streak > N:
            if streak %2 == 0:
                streak -= 1
            result += (streak-N)/2

        if x == "I":
            streak = 1
        else:
            streak = 0

if streak > N:
    if streak %2 == 0:
        streak -= 1
    result += (streak-N)/2

print(int(result))