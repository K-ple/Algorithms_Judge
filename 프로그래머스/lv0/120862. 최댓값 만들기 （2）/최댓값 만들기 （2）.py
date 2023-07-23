def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(1+i, len(numbers)):
            answer.append(numbers[i]*numbers[j])
    return max(answer)