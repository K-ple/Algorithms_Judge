def solution(t, p):
    answer = 0
    a = []
    for i in range(len(t)-len(p)+1):
        a.append('{}'.format(t[i:i+len(p)]))
    
    
    return sum(1 for j in a if int(j) <= int(p)) 