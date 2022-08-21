import sys

n = int(sys.stdin.readline())

for i in range(n):
    k = int(sys.stdin.readline())

    clothes = {}

    for j in range(k):
        case = sys.stdin.readline().rstrip().split()[-1]

        if clothes.get(case) == None:
            clothes[case] = 1
        else:
            clothes[case] += 1

    clothes_list = []

    for key in list(clothes.keys()):
        clothes_list.append(clothes[key])

    result = 1

    for i in range(len(clothes_list)):
        result *= clothes_list[i] + 1
    
    print(result-1)
            
    
