def solution(n):
    answer = []
    if n == 1:
        return [[1]]
    for i in range(n):
        answer.append([0]*n)
    
    a = 1
    x = 0
    y = n
    while a < n**2:
        for i in range(x,y):
            answer[x][i] = a
            a +=1
        for j in range(x+1,y):
            answer[j][y-1] = a
            a+=1
        for k in range(y-2,x-1,-1):
            answer[y-1][k] = a
            a+= 1
        for l in range(y-2,x,-1):
            answer[l][x] = a
            a+= 1
        if n % 2 != 0 and a == n**2:
            answer[n//2][n//2] = a
            break
        x += 1
        y -= 1
    return answer