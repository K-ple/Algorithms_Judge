def solution(arr, k):
    answer = []
    for j in arr:
        if j not in answer:
            answer.append(j)
        if len(answer) == k:
            break
    if len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)
    
    return answer