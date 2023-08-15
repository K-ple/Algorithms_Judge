def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
    if sum(num_list) ** 2 > answer:
        return 1
    else:
        return 0