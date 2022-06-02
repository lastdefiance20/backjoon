import sys
import copy

N = int(sys.stdin.readline())

coordinate = list(map(int, sys.stdin.readline().split()))

coordinate_tmp = copy.deepcopy(coordinate)

convert_dic = {}

coordinate_tmp.sort()

n = 0
tmp = 10**10

for x in coordinate_tmp:
    if x != tmp:
        tmp = x
        convert_dic[x] = n
        n += 1

def convert_coordinate(num):
    return convert_dic[num]

print(" ".join(list(map(str, map(convert_coordinate, coordinate)))))