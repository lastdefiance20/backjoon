import sys

N = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))

card_price = [0 for _ in range(N)]
card_price[0] = card_list[0]

for i in range(1, N):
    value = []
    for j in range(i):
        value.append(card_price[i-j-1]+card_list[j])
    value.append(card_list[i])

    #print(value)
    card_price[i] = max(value)

print(card_price[-1])