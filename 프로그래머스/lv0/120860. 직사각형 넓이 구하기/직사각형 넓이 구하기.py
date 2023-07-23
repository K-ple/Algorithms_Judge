def solution(dots):
    for i in range(1,4):
        if dots[i][1] == dots[0][1]:
            a = dots[i][0] - dots[0][0]
            
        if dots[i][0] == dots[0][0]:
            b = dots[i][1] - dots[0][1]
    if a * b < 0:
        return a*b*-1
    return a*b