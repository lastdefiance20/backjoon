#input 
#재료의 개수
#갑옷 수
#재료 2개 합치면 갑옷수

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

numidx = [0 for x in range(100001)]
queue = list(map(int, sys.stdin.readline().split()))

armor = 0 #armor

for i in queue:
    numidx[i] += 1
    
for j in range(1, 100001):
    if numidx[j] > 0:
        if M-j <= 100000: #out of index 방지
            if numidx[M-j] > 0:
                if j == M-j: #same number add calculation
                    armor += numidx[j]//2
                    numidx[j] = 0
                make = min(numidx[j], numidx[M-j])
                numidx[j] = 0
                numidx[M-j] = 0
                armor += make
            
print(armor)