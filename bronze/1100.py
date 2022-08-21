import sys

result = 0

for i in range(8):
    array = sys.stdin.readline().rstrip()
    if i % 2 == 0:
        for idx in range(0, 8, 2):
            if array[idx] == 'F':
                result += 1
    else:
        for idx in range(1, 8, 2):
            if array[idx] == 'F':
                result += 1

print(result)