import sys

A, B = sys.stdin.readline().split()

def check47(char1, char2):
    ret_val = 0
    for i in range(int(char1), int(char2)+1):
        if i == 7 or i == 4:
            ret_val += 1
    return ret_val

min_len = len(A)
max_len = len(B)

if min_len == max_len:
    result = 1
    for x in range(min_len):
        result *= check47(A[x], B[x])

print(result)