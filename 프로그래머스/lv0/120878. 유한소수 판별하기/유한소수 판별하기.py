def yak(alpha):
    a = []
    for i in range(1,alpha+1):
        if alpha % i == 0:
            a.append(i)
    return a

def solution(a, b):
    answer = 0
    yak_a = yak(a)
    yak_b = yak(b)
    gyo = set(yak_a) & set(yak_b)
    if max(gyo) != 1:
        b = b // max(gyo)
    yak_b = yak(b)
    for i in yak_b[1:]:
        if i % 2 == 0 or i % 5 == 0:
            continue
        else:
            return 2
        
    return 1