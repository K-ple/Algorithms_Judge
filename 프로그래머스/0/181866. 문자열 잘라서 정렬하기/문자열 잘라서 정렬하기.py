def solution(myString):
    answer = myString.split('x')
    answer.sort()
    while answer[0] == '':
        answer.pop(0)
    return answer