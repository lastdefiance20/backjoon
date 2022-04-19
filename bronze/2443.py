#별찍기

n = int(input())

n = n*2-1

for i in range(n, -1, -2):
    for x in range(0, (n-i)//2):
        print(" ", end = '')
    for x in range(0, i):
        print("*", end = '')
    print()