import sys

n = int(sys.stdin.readline())

x = list(sys.stdin.readline().rstrip())

total = 0
exp = 0
M = 1234567891
for i in x:
    total += (ord(i)-96)*(31**exp)
    exp+=1
total = total%M
    
print(total)