def solution(name, yearning, photo):
    answer = []
    for i in photo:
        a = 0
        for j in range(len(name)):
            if name[j] in i:
                a+= yearning[j]
        answer.append(a)
    return answer