import sys

def backpack_algo(maxW, stuff, backpack):
    x = len(stuff)
    
    if x == 0:
        return 0
    
    if backpack[maxW][x] != -1:
        return backpack[maxW][x]
    
    if (maxW-stuff[-1][0]) >= 0:
        backpack[maxW][x] = max(backpack_algo(maxW, stuff[:-1], backpack), 
                                backpack_algo(maxW-stuff[-1][0], stuff[:-1], backpack)+stuff[-1][1])
    else:
        backpack[maxW][x] = backpack_algo(maxW, stuff[:-1], backpack)
            
    if backpack[maxW][x] == -1:
        backpack[maxW][x] = 0
    return backpack[maxW][x]

#weight, value
stuff = []

n, maxW = map(int, sys.stdin.readline().split())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    stuff.append([a, b])
    
#store result
backpack = [[-1 for y in range(len(stuff)+1)] for x in range(maxW+1)]

print(backpack_algo(maxW, stuff, backpack))