def solution(a, d, included):
    answer = 0
    for i in included:
        if int(i) == 1:
            answer += a
        a += d
    return answer