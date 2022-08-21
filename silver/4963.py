import sys

def check_bound(y, x, h, w):
    if y < 0 or y >= h:
        return False
    elif x < 0 or x >= w:
        return False
    else:
        return True

while True:
    w, h = map(int, sys.stdin.readline().split())

    #break if 0, 0
    if w == 0 and h == 0:
        break

    map_list = []

    for y in range(h):
        map_list.append(list(map(int, sys.stdin.readline().split())))

    map_count = 0

    for y in range(h):
        for x in range(w):
            if map_list[y][x] == 1:
                map_count+=1
                #dfs
                stack = []
                map_list[y][x] = 0
                stack.append((y, x))
                while len(stack):
                    #print(stack)
                    y1, x1 = stack.pop()
                    for q in [y1-1, y1, y1+1]:
                        for p in [x1-1, x1, x1+1]:
                            #print(q,p)
                            if check_bound(q, p, h, w):
                                if map_list[q][p] == 1:
                                    map_list[q][p] = 0
                                    stack.append((q, p))
    print(map_count)