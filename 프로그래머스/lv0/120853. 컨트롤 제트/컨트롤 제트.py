def solution(s):
    a = []
    for i in s.split():
        if i =='Z':
            a.pop(-1)
        else:
            a.append(i)
    return sum(map(int, a))