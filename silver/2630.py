import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    array.append(tmp)

def check_four(arr, x, y, n):
    result = 0
    half_n = n//2

    result += check_color(arr, x, y, half_n)
    result += check_color(arr, x+half_n, y, half_n)
    result += check_color(arr, x, y+half_n, half_n)
    result += check_color(arr, x+half_n, y+half_n, half_n)

    if result < 0:
        return (check_four(arr, x, y, half_n) 
                + check_four(arr, x+half_n, y, half_n) 
                + check_four(arr, x, y+half_n, half_n)
                + check_four(arr, x+half_n, y+half_n, half_n))
    elif result == 4:
        return(1, 0)

    elif result == 0:
        return(0, 1)
    else:
        return (result, 4-result)


def check_color(arr, x, y, n):
    result = 0
    for j in range(n):
        for k in range(n):
            result += arr[x+k][y+j]

    if result == n*n:
        return 1
    elif result == 0:
        return 0
    else:
        return -10
        
result = check_four(array, 0, 0, N)

answer = [0, 0]

for n in range(len(result)):
    if n%2 == 0:
        answer[0] += result[n]
    else:
        answer[1] += result[n]

print(answer[1])
print(answer[0])