import sys

def isbalance(check_str):
    check_list = []

    for char in check_str:
        if char == "[":
            check_list.append("[")
        elif char == "(":
            check_list.append("(")
        elif char == "]":
            if len(check_list) == 0:
                return False
            else:
                if check_list[-1] == "[":
                    check_list.pop()
                else:
                    return False
        elif char == ")":
            if len(check_list) == 0:
                return False
            else:
                if check_list[-1] == "(":
                    check_list.pop()
                else:
                    return False

    if len(check_list) == 0:
        return True
    else:
        return False


while True:
    check_str = sys.stdin.readline().rstrip()

    #if input == '.', end the program
    if check_str == ".":
        break

    if isbalance(check_str):
        print("yes")
    else:
        print("no")