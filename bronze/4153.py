import sys
while(1):
    x = list(map(int, sys.stdin.readline().split()))
    if(sum(x) == 0): break
    x.sort()
    if(x[2]*x[2] == x[1]*x[1]+x[0]*x[0]):
        print("right")
    else:
        print("wrong")