def solution(a, b, c, d):
    answer = 0
    check = [a,b,c,d]
    if check.count(a) == len(check):
        return a*1111
    else:
        count = 0
        for i in check:
            a = check.count(i)
            if a > count:
                count = a
        check.sort()
        if count == 3:
            if check[0] == check[1]:
                return (10*check[0]+check[3])**2
            else:
                return (check[0]+10*check[3])**2
        if count == 2:
            if check[0] == check[1]:
                if check[2] == check[3]:
                    return (check[0]+check[2])*abs(check[0]-check[2])
                else:
                    return check[2]*check[3]
            elif check[1] == check[2]:
                return check[0]*check[3]
            else:
                return check[0]*check[1]
        else:
            return check[0]
    return answer