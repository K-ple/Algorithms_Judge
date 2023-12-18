def solution(num_list, n):
    answer = []
    num = 0
    while num < len(num_list):
        answer.append(num_list[num])
        num += n
    return answer