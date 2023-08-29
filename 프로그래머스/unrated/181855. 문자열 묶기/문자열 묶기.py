def solution(strArr):
    l = [0]*31
    for i in strArr:
        l[len(i)] += 1

    return max(l)