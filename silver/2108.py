import sys

val_array = [0 for x in range(8001)]

sum = 0
max_val = 0
mid_val = 0
min_val = 0

first_val = True
first_mid = True

n = int(sys.stdin.readline())

mid_idx = (n-1)/2
sum_idx = 0

max_count = 0
max_count_list = []

for i in range(n):
    x = int(sys.stdin.readline())
    val_array[x+4000] += 1

for idx in range(8001):
    if val_array[idx] == 0:
        continue

    if first_val == True:
        min_val = (idx-4000)
        first_val = False

    sum += (idx-4000)*val_array[idx]
    max_val = (idx-4000)
    sum_idx += val_array[idx]

    if max_count <= val_array[idx]:
        if max_count == val_array[idx]:
            max_count_list.append(idx-4000)
        else:
            max_count_list = [idx-4000]
            max_count = val_array[idx]

    if sum_idx > mid_idx:
        if first_mid == True:
            mid_val = (idx-4000)
            first_mid = False


average = round(sum/n)
print(average)

print(mid_val)

if len(max_count_list) == 1:
    print(max_count_list[0])
else:
    max_count_list.sort()
    print(max_count_list[1])

val_range = max_val - min_val
print(val_range)
