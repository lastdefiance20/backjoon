import sys

sub_list = sys.stdin.readline().rstrip().split("-")

for idx in range(len(sub_list)):
    add_list = sub_list[idx].split("+")
    sum_num = 0
    for num in add_list:
        sum_num += int(num)
    sub_list[idx] = sum_num

result = 0

for idx in range(len(sub_list)):
    if idx == 0:
        result = sub_list[idx]
    else:
        result -= sub_list[idx]

print(result)