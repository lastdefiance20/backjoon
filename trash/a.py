import collections

def bfs_search(n, m, grid, k):
    been_searched = []

    for i in range(n+1):
        been_searched.append([5000 for j in range(m+1)])

    restore = k
    energy = k # eg
    sleep_count = 0 # sc

    # distance from last camping = camp_distance
    camp_distance = 1 # cd

    queue = collections.deque([[0, 0, energy, camp_distance, sleep_count]])

    while queue:
        x, y, eg, cd, sc = queue.popleft()

        #check if searched
        if been_searched[x][y] > sc:
            been_searched[x][y] = sc

            rest_able = grid[x][y] == "."

            if eg == 0:
                if rest_able:
                    eg += restore
                    sc += 1
                else:
                    eg += restore - cd
                    sc += 1
            
            #check energy
            if eg > 0:
                x_inv = x-1 >= 0
                x_inf = x+1 <= n
                y_inv = y-1 >= 0
                y_inf = y+1 <= m

                if rest_able:
                    cd = 0

                if x_inv:
                    if grid[x-1][y] != "#":
                        queue.append([x-1, y, eg-1, cd+1, sc])

                if x_inf:
                    if grid[x+1][y] != "#":
                        queue.append([x+1, y, eg-1, cd+1, sc])
                
                if y_inv:
                    if grid[y-1][y] != "#":
                        queue.append([x, y-1, eg-1, cd+1, sc])

                if y_inf:
                    if grid[y+1][y] != "#":
                        queue.append([x, y+1, eg-1, cd+1, sc])

                print(queue)

    print(been_searched)

    return been_searched[n][m]

def solution(grid, k):
    # using DFS / BFS

    # move at "." or "F", can't cross "#""

    #need to sleep at "." -> restore energy k

    tmp_2d = []

    for grid_char in grid:
        tmp = []

        for char in grid_char:
            tmp.append(char)

        tmp_2d.append(tmp)

    grid = tmp_2d
    
    n = len(grid)-1
    m = len(grid[0])-1

    answer = bfs_search(n, m, grid, k)
    return answer

print(solution([["..FF"],["###F"],["###."]], 4))