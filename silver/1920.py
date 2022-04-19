import sys

N = sys.stdin.readline()

queue = list(sys.stdin.readline().split())

int_dic = {"100":100}

for i in queue:
    int_dic[i] = i
    
M = sys.stdin.readline()

queue = list(sys.stdin.readline().split())

for i in queue:
    if i in int_dic:
        print(1)
    else:
        print(0)