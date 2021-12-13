import sys
import copy
n = int(sys.stdin.readline())

card = [x for x in range(1, n+1)]
index = 1

while(1):
    tmp = []
    if(len(card) == 1):
        print(card[0])
        break
    for i in range(index, len(card), 2):
        tmp.append(card[i])
    if(i == len(card)-1):
        index = 1
    else:
        index = 0
    card = copy.deepcopy(tmp)


#시간초과, 위처럼 타노스 반반 전법 사용
'''
card = [x for x in range(1, n+1)]
index = 0

while(1):
    index = index%(len(card))
    if(len(card) == 1): 
        print(card[0])
        break
    del card[index]
    index += 1
'''