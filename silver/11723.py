import sys
set_list = [0 for x in range(21)]

M = int(sys.stdin.readline())
for i in range(M):
    msg = sys.stdin.readline().split()
    if msg[0] == "add":
        set_list[int(msg[1])] = 1
    elif msg[0] == "remove":
        set_list[int(msg[1])] = 0
    elif msg[0] == "check":
        if set_list[int(msg[1])] == 1:
            print(1)
        else:
            print(0)
    elif msg[0] == "toggle":
        if set_list[int(msg[1])] == 1:
            set_list[int(msg[1])] = 0
        else:
            set_list[int(msg[1])] = 1
    elif msg[0] == "all":
        set_list = [1 for x in range(21)]
    elif msg[0] == "empty":
        set_list = [0 for x in range(21)]
