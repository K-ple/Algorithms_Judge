def solution(array, commands):
    answer = []
    for i in commands:
        if i[0] == i[1]:
            answer.append(array[i[0]-1])
            continue
        a = array[i[0]-1:i[1]]
        a.sort()
        answer.append(a[i[2]-1])
    return answer