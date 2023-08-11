def solution(s):
    first_switch = 0
    for i in s:
        if i == '(':
            first_switch += 1
        else:
            first_switch -= 1
        
        if first_switch < 0:
            return False
    if first_switch == 0 and s[-1] == ')':
        return True
    else:
        return False