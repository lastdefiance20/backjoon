import sys

n = int(sys.stdin.readline())

coordinate_dic = {}
coordinate_x = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    try:
        coordinate_dic[x].append(y)
    except:
        coordinate_dic[x] = [y]
        coordinate_x.append(x)

coordinate_x.sort()

for x in coordinate_x:
    coordinate_y = coordinate_dic[x]
    coordinate_y.sort()
    for y in coordinate_y:
        print(x, y)