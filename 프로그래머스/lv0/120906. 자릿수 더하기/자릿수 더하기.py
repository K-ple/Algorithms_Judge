def solution(n):
    answer = 0
    a = str(n)
    return sum(int(a[i]) for i in range(len(a)))