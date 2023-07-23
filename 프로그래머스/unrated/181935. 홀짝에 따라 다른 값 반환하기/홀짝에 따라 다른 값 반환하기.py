def solution(n):
    answer = 0
    if n % 2 == 1:
        answer += n
        for i in range(n):
            if i % 2 == 1:
                answer += i
            
        
    elif n % 2 == 0:
        answer += n**2
        for j in range(n):
            if j % 2 == 0:
                answer += j**2
    return answer