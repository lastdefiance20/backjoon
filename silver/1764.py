import sys

N, M = map(int, sys.stdin.readline().split())

dic = {}

no_heard_seen = []

for i in range(N):
    name = sys.stdin.readline().rstrip()
    dic[name] = 1

for i in range(M):
    name = sys.stdin.readline().rstrip()
    try:
        dic[name]
        no_heard_seen.append(name)

    except:
        pass

print(len(no_heard_seen))
no_heard_seen.sort()
for name in no_heard_seen:
    print(name)