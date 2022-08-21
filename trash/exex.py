def up_idx(select, n, table):
    while n:
        select -= 1
        if select < 0:
            return -1
        if table[select] == 'O':
            n -= 1
    return select

def down_idx(select, n, table, bound):
    while n:
        select += 1
        if select >= bound:
            return -1
        if table[select] == 'O':
            n -= 1
            
    return select

def solution(n, k, cmd):
    select = k
    recover_stack = []
    table = ['O' for _ in range(n)]
    
    for command in cmd:
        command_type = command[0]
        
        if command_type == "U":
            select = up_idx(select, int(command.split()[1]), table)
                                                  
        elif command_type == "D":
            select = down_idx(select, int(command.split()[1]), table, n)
            
        elif command_type == "C":
            recover_stack.append(select)
            table[select] = 'X'
            
            tmp_select = down_idx(select, 1, table, n)
            if tmp_select == -1:
                select = up_idx(select, 1, table)
            else:
                select = tmp_select
                                                  
        else:
            table[recover_stack.pop()] = 'O'
            
        #print(table)
    
    answer = ''.join(table)
    return answer

# n = 표의 행 개수, k = 선택된 행의 위치, cmd = 명령어 문자열

# 표의 행을 선택, 삭제, 복구하는 프로그램

# 파란색 = 선택된 행, 한번에 한 행만 선택가능

# U X = 선택칸 X칸 위에 있는 행 선택
# D X = 선택된 행 X칸 아래에 있는 행 선택
# C = 선택된 행 삭제 이후 바로 아래 행 선택 (마지막행일 경우 바로 윗 행 선택)
# Z = 가장 최근에 삭제된 행을 원래대로 복구. 단 현재 선택된 행은 바뀌지 않음