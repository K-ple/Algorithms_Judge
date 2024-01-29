def solution(my_string, m, c):
    
    li = []
    count = m
    for i in range(len(my_string)//m):
        li.append(my_string[i*m:count])
        count += m
    return ''.join([i[c-1] for i in li])