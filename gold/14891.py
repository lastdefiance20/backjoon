import sys

class gear():
    def __init__(self, gearlist):
        self.gearlist = gearlist
        self.scoreidx = 0
        self.leftidx = 6
        self.rightidx = 2

    def spin(self, num):
        self.scoreidx = (self.scoreidx-num)%8
        self.leftidx = (self.leftidx-num)%8
        self.rightidx = (self.rightidx-num)%8

    def state(self):
        left_val = self.gearlist[self.leftidx]
        right_val = self.gearlist[self.rightidx]
        return (left_val, right_val)

    def score(self):
        if self.gearlist[self.scoreidx] == 1:
            return 1
        else:
            return 0
    
    #for debug
    def printidx(self):
        print(self.scoreidx)

gear_list_2d = []
for i in range(4):
    gear_info = sys.stdin.readline().rstrip()
    gear_list = []
    for info in gear_info:
        gear_list.append(int(info))
    gear_list_2d.append(gear_list)

gear_1 = gear(gear_list_2d[0])
gear_2 = gear(gear_list_2d[1])
gear_3 = gear(gear_list_2d[2])
gear_4 = gear(gear_list_2d[3])

gear_set = [gear_1, gear_2, gear_3, gear_4]

k = int(sys.stdin.readline().rstrip())
#회전 횟수 k개
for i in range(k):
    gear_spin = [0 for x in range(4)]

    gear_num, spin = map(int, sys.stdin.readline().split())
    gear_num -= 1

    gear_spin[gear_num] = spin

    gear_search = [[gear_num + 1, gear_num], [gear_num - 1, gear_num]]
    while gear_search:
        target, source = gear_search.pop()
        if (target < 0 or 3 < target):
            continue
        #target의 오른쪽, source 왼쪽 비교. target 왼쪽 톱니 추가
        if target < source:
            if gear_set[target].state()[1] != gear_set[source].state()[0]:
                gear_search.append([target - 1, target])
                gear_spin[target] = gear_spin[source] * -1

        #target의 왼쪽, source 오른쪽 비교. source 왼쪽 추가
        else:
            if gear_set[target].state()[0] != gear_set[source].state()[1]:
                gear_search.append([target + 1, target])
                gear_spin[target] = gear_spin[source] * -1

    #spin 적용
    #print(gear_spin)
    for idx in range(4):
        gear_set[idx].spin(gear_spin[idx])

score = 0
for idx in range(4):
    score += gear_set[idx].score()*(2**idx)

print(score)