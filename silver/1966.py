import sys

n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    
    queue = list(map(int, sys.stdin.readline().split()))
    trace = [0 for j in range(x)]
    trace[y] = 1
    
    printnum = 0

    while True:
        document = queue[0]
        dtrace = trace[0]
        if document < max(queue):
            queue.pop(0)
            trace.pop(0)
            queue.append(document)
            trace.append(dtrace)
        else:
            queue.pop(0)
            trace.pop(0)
            printnum += 1
            if dtrace == 1:
                print(printnum)
                break
