def solution(n, control):
    for i in control:
        if i is "w":
            n += 1
        elif i is 's':
            n -= 1
        elif i is 'd':
            n += 10
        elif i is 'a':
            n -= 10
    return n