def solution(spell, dic):
    answer = 0
    for i in dic:
        for j in spell:
            if j in i:
                answer = 1
            else:
                answer = 2
                break
        if answer == 1:
            break
    return answer