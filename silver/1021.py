#큐의 크기 N, 뽑을 개수 M
#뽑아내려는 수의 위치

#뽑아내기 위해서 수행하는 연산 최솟값 출력

import sys

def spin_left(queue):
    tmp = queue.pop(0)
    queue.append(tmp)
    
def spin_right(queue):
    tmp = queue.pop(-1)
    queue.insert(0, tmp)

N, M = map(int, sys.stdin.readline().rstrip().split())

pop_list = list(map(int, sys.stdin.readline().split()))

spin_queue = [x for x in range(1, N+1)]

spin_num = 0

for pop_val in pop_list:
    idx = 0
    for i in range(len(spin_queue)):
        if pop_val == spin_queue[i]:
            break
        idx += 1
    if idx == 0:
        spin_queue.pop(0)
    else:
        if idx/len(spin_queue)<0.5:
            while True:
                spin_left(spin_queue)
                spin_num+=1
                if pop_val == spin_queue[0]:
                    spin_queue.pop(0)
                    break
        else:
            while True:
                spin_right(spin_queue)
                spin_num+=1
                if pop_val == spin_queue[0]:
                    spin_queue.pop(0)
                    break
                
print(spin_num)
        