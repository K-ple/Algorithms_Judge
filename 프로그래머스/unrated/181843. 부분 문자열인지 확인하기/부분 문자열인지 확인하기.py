def solution(my_string, target):
    answer = 0
    l = len(target)
    for i in range(len(my_string)-l+1):
        for j in range(l):
            if my_string[i:i+j+1] == target:
                answer = 1
                break
                
    return 1 if answer == 1 else 0