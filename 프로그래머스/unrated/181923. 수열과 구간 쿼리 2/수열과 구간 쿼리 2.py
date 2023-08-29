def solution(arr, queries):
    answer = []
    for j in queries:
        a, b, c = j
        d = [i for i in arr[a:b+1] if i > c]
        if len(d) == 0:
            answer.append(-1)
            continue
        answer.append(min(d))
    return answer