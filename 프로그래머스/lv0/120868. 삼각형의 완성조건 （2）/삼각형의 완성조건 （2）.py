def solution(sides):
    a = []
    for i in range(max(sides)+1):
        if max(sides) < i + min(sides) and i <= max(sides):
            a.append(i)
    for i in range(sum(sides)):
        if sum(sides) > i > max(sides):
            a.append(i)
    return len(a)