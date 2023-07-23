def solution(chicken):
    a = []
    na = 0
    for i in range(6):
        chicken += na
        if chicken >= 10:
            na = chicken % 10
            a.append(chicken//10)
            chicken = chicken//10
            
        else:
            break
    return sum(a)