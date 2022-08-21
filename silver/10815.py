import sys

sys.stdin.readline()
card_list = list(sys.stdin.readline().split())
sys.stdin.readline()
check_list = list(sys.stdin.readline().split())

card_deck = {}

for card in card_list:
    card_deck[card] = 1

result = []
for card in check_list:
    if card in card_deck:
        result.append('1')
    else:
        result.append('0')

print(" ".join(result))