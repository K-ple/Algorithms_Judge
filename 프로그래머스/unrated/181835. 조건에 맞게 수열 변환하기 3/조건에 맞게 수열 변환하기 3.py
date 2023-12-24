def solution(arr, k):
    answer = []
    tf = 1 if k % 2 != 0 else 0
    if tf:
        for i in arr:
            answer.append(i*k)
    else:
        for i in arr:
            answer.append(i+k)
    return answer