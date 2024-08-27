def solution(X, Y):
    s1 = {}
    s2 = {}
    for i in X:
        if i not in s1:
            s1[i] = 1
        else:
            s1[i] += 1
    for i in Y:
        if i not in s2:
            s2[i] = 1
        else:
            s2[i] += 1
            
    check = []
    for i,j in s1.items():
        if i in s2:
            for _ in range(min([j,s2[i]])):
                check.append(i)
    if check == []:
        return '-1'
    if sum(map(int, check)) == 0:
        return '0'
    check.sort(reverse = True)
    return ''.join(i for i in check)