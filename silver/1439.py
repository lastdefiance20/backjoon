import sys

char_arr = sys.stdin.readline().rstrip()

save_char = char_arr[0]

changed_time = 1

for x in char_arr:
    if x != save_char:
        save_char = x
        changed_time += 1

print(changed_time//2)