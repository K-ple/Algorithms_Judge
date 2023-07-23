def solution(a, b):
    answer = 0
    first = 0
    second = 0
    first = str(a) + str(b)
    second = str(b) + str(a)
    if int(first) > int(second):
        answer += int(first)
    elif int(second) > int(first):
        answer += int(second)
    else:
        answer += int(first)
    return answer