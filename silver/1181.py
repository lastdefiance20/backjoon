import sys

n = int(sys.stdin.readline())

word_list = [list() for x in range(51)]

for i in range(n):
    word = sys.stdin.readline().rstrip()
    word_list[len(word)].append(word)

for idx in range(51):
    word_list[idx].sort()

for idx in range(51):
    if word_list[idx] != None:
        tmp = " "
        for word in word_list[idx]:
            if word != tmp:
                print(word)
                tmp = word