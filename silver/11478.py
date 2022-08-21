import sys

str = sys.stdin.readline()
set_str = set()
len_str = len(str)

for i in range(1, len_str+1):
    j = 0
    while j+i != len_str:
        set_str.add(str[j:j+i])
        j += 1

print(len(set_str))