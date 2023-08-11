def solution(s):
    check = []
    for i in s:
        if i not in check:
            check.append(i)
        else:
            if i == check[-1]:
                check.pop()
            else:
                check.append(i)
    
    if check == []:
        return 1
    else:
        return 0