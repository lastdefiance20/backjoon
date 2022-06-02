import sys

n = int(sys.stdin.readline())

stair = [0]

for i in range(n):
    score = int(sys.stdin.readline())
    stair.append(score)

max_score = 0

memory = [[0 for x in range(3)]for x in range(301)]

dfs_queue = [(0,0,0)]

while dfs_queue:
    #print(dfs_queue)

    stairidx, streak, score = dfs_queue.pop(0)

    if memory[stairidx][streak] != score:
        continue

    if stairidx == n:
        if score > max_score:
            max_score = score
    else:
        if streak != 2:
            if memory[stairidx+1][streak+1] < score+stair[stairidx+1]:
                memory[stairidx+1][streak+1] = score+stair[stairidx+1]
                dfs_queue.append((stairidx+1, streak+1, score+stair[stairidx+1]))

        if stairidx+1 == n:
            if streak != 2:
                if score > max_score:
                    max_score = score
        else:
            if memory[stairidx+2][1] < score+stair[stairidx+2]:
                memory[stairidx+2][1] = score+stair[stairidx+2]
                dfs_queue.append((stairidx+2, 1, score+stair[stairidx+2]))

print(max_score)