def solution(a, b):
    answer = 0
    first = 0
    second = 0
    first = str(a) + str(b)
    answer = int(max(int(first), 2 * a * b))
    return answer