def solution(names):
    answer = []
    first = 0
    while len(names) > first:
        answer.append(names[first])
        first += 5
    return answer