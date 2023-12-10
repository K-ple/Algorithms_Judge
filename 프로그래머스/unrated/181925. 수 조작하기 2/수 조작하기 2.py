def solution(numLog):
    answer = ''
    num = numLog[0]
    for i in numLog:
        if num + 1 == i:
            answer += 'w'
        elif num + 10 == i:
            answer += 'd'
        elif num - 1 == i:
            answer += 's'
        else:
            answer += 'a'
        num = i
    return answer[1:]