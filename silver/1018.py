import sys

N, M = map(int, sys.stdin.readline().split())

def checkRepaintNeeded(chessarr, x, y):
    repaint1 = 0
    repaint2 = 0

    for yidx in range(y, 8+y):
        for xidx in range(x, 8+x):
            if (xidx+yidx) %2 == 0:
                if chessarr[yidx][xidx] != "W":
                    repaint1 += 1
                else:
                    repaint2 += 1
            else:
                if chessarr[yidx][xidx] != "B":
                    repaint1 += 1
                else:
                    repaint2 += 1

    if repaint2 > repaint1:
        return repaint1
    else:
        return repaint2

chessarr = []

for i in range(N):
    tmparr = []

    for tmp in sys.stdin.readline().rstrip():
        tmparr.append(tmp)

    chessarr.append(tmparr)

minval = 8*8

for y in range(N-7):
    for x in range(M-7):
        tmp = checkRepaintNeeded(chessarr, x, y)
        if minval > tmp:
            minval = tmp

print(minval)