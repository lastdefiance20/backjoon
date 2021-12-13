def check_p(word):
    for i in range(len(word)//2+1):
        if word[i] == word[len(word)-i-1]:
            pass
        else:
            print("no")
            return 0
    print("yes")
    return 1

while(1):
    word = list(input())
    if (word[0] == '0')and(len(word) == 1):
        break
    check_p(word)