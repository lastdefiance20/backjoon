import sys

def find_str(z):
    z_len = len(z)+1
    i = 0
    while z_len+i <= len(string):
        if string[1+i:z_len+i] == z:
            return 1
        i += 1
    return 0

n = sys.stdin.readline().rstrip()

string = 'S'

for x in n:
    if (47<ord(x)<58): #파이썬 in 탐색은 느리다?, 아스키 사용
        pass
    else:
        string += x

z = sys.stdin.readline().rstrip()

print(find_str(z))