import sys

n = int(sys.stdin.readline())

coordinate_dic = {}
coordinate_y = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    try:
        coordinate_dic[y].append(x)
    except:
        coordinate_dic[y] = [x]
        coordinate_y.append(y)

coordinate_y.sort()

for y in coordinate_y:
    coordinate_x = coordinate_dic[y]
    coordinate_x.sort()
    for x in coordinate_x:
        print(x, y)