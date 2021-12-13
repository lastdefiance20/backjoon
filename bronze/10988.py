def check_p(word):
    for i in range(len(word)//2+1):
        if word[i] == word[len(word)-i-1]:
            pass
        else:
            return 0
    return 1

word = list(input())
print(check_p(word))