def solution(progresses, speeds):
    answer = []
    check = []
    for i in range(len(progresses)):
        n = 100 - progresses[i]
        if n % speeds[i] == 0:
            k = n//speeds[i]
        else:
            k = n//speeds[i]+1
        if len(check) == 0 or check[-1] < k:
            answer.append(1)
            check.append(k)    
        else:
            answer[-1] += 1
        
    return answer