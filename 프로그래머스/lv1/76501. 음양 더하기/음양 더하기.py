def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] is False:
            absolutes[i] = absolutes[i] * -1
            
    return sum(absolutes)