import sys

def factorial(i):
    if(i <= 1):
        return 1
    else:
        return i * factorial(i-1)

x, y = map(int, sys.stdin.readline().split())
print(int(factorial(x)/(factorial(x-y)*factorial(y))))