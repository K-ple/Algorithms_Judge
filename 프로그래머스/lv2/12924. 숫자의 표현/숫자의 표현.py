def solution(n):
    answer = 0
    for i in range(1,n+1):
        check = 0
        for j in range(i, n+1):
            check += j
            if check == n:
                answer += 1
                break

            elif check > n:
                break
    return answer