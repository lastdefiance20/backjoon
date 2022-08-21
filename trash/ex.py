from collections import deque

def check_bound(x, y):
    if x < 0 or x > 100:
        return False
    elif y < 0 or y > 100:
        return False
    else:
        return True

def BFS(array, start_x, start_y, end_x, end_y):
    start_x *= 2
    start_y *= 2
    end_x *= 2
    end_y *= 2
    
    deq = deque()
    deq.append((start_x, start_y, 0))
    array[start_y][start_x] = 0
    len_deq = 1
    
    while len_deq:
        x, y, move = deq.popleft()
        len_deq -= 1
        
        if x == end_x and y == end_y:
            return move
        
        for tmp_x, tmp_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if check_bound(tmp_x, tmp_y):
                if array[tmp_y][tmp_x] != 0:
                    deq.append((tmp_y, tmp_x, move+1))
                    array[tmp_y][tmp_x] = 0
                    len_deq += 1
        print(deq)

def solution(rectangle, characterX, characterY, itemX, itemY):
    array = [[0 for _ in range(40)] for _ in range(40)]
    
    # drow rectangle
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        for x in range(x1, x2+1):
            array[y1][x] = 1
            array[y2][x] = 1
        for y in range(y1, y2+1):
            array[y][x1] = 1
            array[y][x2] = 1      

    # delete point inside rectangle
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        for x in range(x1+1, x2):
            array[y1+1][x] = 0
            array[y2-1][x] = 0
        for y in range(y1+1, y2):
            array[y][x1+1] = 0
            array[y][x2-1] = 0

    for arr in array:
        print(arr)
    
    answer = BFS(array, characterX, characterY, itemX, itemY)
    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))