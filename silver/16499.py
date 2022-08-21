import sys

n = int(sys.stdin.readline())

setlist = []

result = 0

for i in range(n):
    word = sys.stdin.readline().rstrip()
    tmpset = set([])
    for char in word:
        while char in tmpset:
            char = char*2
        tmpset.add(char)
    setlist.append(tmpset)

for i in range(len(setlist)):
    if setlist[i] != 0:
        comp = setlist[i]
        setlist[i] = 0
        result += 1
        for idx in range(len(setlist)):
            if setlist[idx] != 0:
                if (len(setlist[idx] - comp) == 0) and (len(comp - setlist[idx]) == 0):
                    setlist[idx] = 0

print(result)