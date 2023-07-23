def solution(a, b):
    if b > a:
        return sum([i for i in range(a,b+1)])
    else:
        return sum([i for i in range(b,a+1)])