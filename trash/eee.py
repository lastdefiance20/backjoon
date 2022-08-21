class node:
    def __init__(self, num):
        self.num = num
        self.next = -1
        self.prev = -1

def up_idx(select, n):
    for i in range(n):
        select = select.prev
    return select

def down_idx(select, n):
    for i in range(n):
        select = select.next
    return select

def check_down(select):
    if select.next == -1:
        return False
    else:
        return True
        
def solution(n, k, cmd):
    class node:
        def __init__(self, num):
            self.num = num
            self.next = -1
            self.prev = -1

    select = k
    recover_stack = []
    table = [node(x) for x in range(n)]
    
    table[0].next = table[1]
    table[-1].prev = table[-2]
    
    for i in range(1, n-1):
        table[i].next = table[i+1]
        table[i].prev = table[i-1]
        
    select = table[select]
    
    for command in cmd:
        command_type = command[0]
        
        if command_type == "U":
            select = up_idx(select, int(command.split()[1]))
                                                  
        elif command_type == "D":
            select = down_idx(select, int(command.split()[1]))
            
        elif command_type == "C":
            recover_stack.append((select.num, select.next, select.prev))
            select.num = 0
            
            if select.prev == -1:
                select.next.prev = -1
                
            elif select.next == -1:
                select.prev.next = -1
            
            else:
                select.next.prev = select.prev
                select.prev.next = select.next
                                      
            if select.prev == -1:
                select = select.next
            else:
                select = select.prev
                                                  
        else:
            num, node_next, node_prev = recover_stack.pop()
            node = table[num]
            print(num, node_next, node_prev)
            node_next.prev = node
            node_prev.next = node
            
    answer = []
    for idx in range(n):
        if table[idx].num != 0:
            answer.append('O')
        else:
            answer.append('X')
    return ''.join(answer)

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])