import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()
len_deq = 0

for _ in range(N):
    cmd_line = sys.stdin.readline().split()
    cmd = cmd_line[0]

    if cmd == 'push':
        deq.append(int(cmd_line[1]))
        len_deq += 1

    elif cmd == 'pop':
        if len_deq > 0:
            print(deq.popleft())
            len_deq -= 1
        else:
            print(-1)

    elif cmd == 'size':
        print(len_deq)

    elif cmd == "empty":
        if len_deq == 0:
            print(1)
        else:
            print(0)

    elif cmd == 'front':
        if len_deq > 0:
            print(deq[0])
        else:
            print(-1)

    elif cmd == 'back':
        if len_deq > 0:
            print(deq[-1])
        else:
            print(-1)
    