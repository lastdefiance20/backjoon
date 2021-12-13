import sys
import math

def fly(distance):
    count = 0
    
    cycle = int(math.sqrt(distance))
    count += cycle*2 - 1
    remain = distance - cycle*cycle
    
    for x in range(cycle, 0, -1):
        if(remain>=x):
            count += remain//x
            remain -= (remain//x)*x
        if(remain == 0):
            break
    
    print(count)

n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    fly(y-x)