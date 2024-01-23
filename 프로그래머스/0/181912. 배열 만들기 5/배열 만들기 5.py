def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        ind = int(i[s:s+l])
        if ind > k:
            answer.append(ind)
    return answer