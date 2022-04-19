#팩토리얼 5가 나눠지는 수의 개수를 세면된다

def check5(num):
    check = 0
    while True:
        remainder = num%5
        if remainder == 0:
            check+=1
            num/=5
        else:
            break
    return check

N = int(input())

num_of_0 = 0

if N == 0:
    print(num_of_0)
else:
    for i in range(1, N+1):
        num_of_0+=check5(i)
    print(num_of_0)