def solution(num_list, n):
    a = []
    answer = []
    for i in num_list:
        a.append(i)
        if len(a) % n == 0:
            answer.append(a)
            a = []
    return answer