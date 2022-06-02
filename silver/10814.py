import sys

n = int(sys.stdin.readline())

member_list = [[] for x in range(201)]

for i in range(n):
    age, name = sys.stdin.readline().split()
    member_list[int(age)].append(name)

for age in range(1, 201, 1):
    if len(member_list[age]) != 0:
        for member in member_list[age]:
            print(age, member)