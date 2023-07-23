def solution(my_str, n):
    answer = []
    if len(my_str) <= n:
        return [my_str] 
    for i in range(len(my_str)//n+1): 
        if len(my_str) == len(''.join(answer)):
            break
        if i == 0:
            answer.append(my_str[:n])
        elif len(my_str[i*n:]) <=n:
            answer.append(my_str[i*n:])
        else:
            answer.append(my_str[i*n:i*n+n])
    return answer