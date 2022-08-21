def up_idx(select, n, index_table):
    index_select = index_table.index(select)
    return index_table[index_select - n]

def down_idx(select, n, index_table):
    index_select = index_table.index(select)
    return index_table[index_select - n]

def check_down(select, index_table):
    if select == index_table[-1]:
        return False
    else:
        return True

def solution(n, k, cmd):
    select = k
    recover_stack = []
    table = ['O' for _ in range(n)]
    index_table = [idx for idx in range(n)]
    
    for command in cmd:
        command_type = command[0]
        
        if command_type == "U":
            select = up_idx(select, int(command.split()[1]), index_table)
                                                  
        elif command_type == "D":
            select = down_idx(select, int(command.split()[1]), index_table)
            
        elif command_type == "C":
            index_table_idx = index_table.index(select)
            recover_stack.append((select, index_table.pop(index_table_idx), index_table_idx))
            table[select] = 'X'
            
            if check_down(select, index_table):
                select = down_idx(select, 1, index_table)
            else:
                select = up_idx(select, 1, index_table)
                                                  
        else:
            idx, index_table_content, index_table_idx = recover_stack.pop()
            table[idx] = 'O'
            index_table.insert(index_table_idx, index_table_content)
            
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