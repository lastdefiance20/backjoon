import sys

card_dic = {}

N = int(sys.stdin.readline().rstrip())

card_list = map(int, sys.stdin.readline().split())

for card in card_list:
    if card in card_dic:
        card_dic[card] += 1
    else:
        card_dic[card] = 1

M = int(sys.stdin.readline().rstrip())

check_list = map(int, sys.stdin.readline().split())

card_count = []

for card in check_list:
    if card in card_dic:
        card_count.append(card_dic[card])
    else:
        card_count.append(0)

print(" ".join(map(str, card_count)), end = "")