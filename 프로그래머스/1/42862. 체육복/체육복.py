def solution(n, lost, reserve):
    answer = 0
    for i in range(1,n+1):

        if i in lost:
            if i in reserve:
                reserve[reserve.index(i)] = -99
                answer += 1
                continue
            if i-1 in reserve and i-1 not in lost:                    
                reserve[reserve.index(i-1)] = - 99
                answer += 1
                continue
            if i+1 in reserve and i+1 not in lost:
                reserve[reserve.index(i+1)]= -99
                answer += 1
                continue
        else:
            answer +=1     
    return answer