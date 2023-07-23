def solution(record):
    answer = []
    code = []
    online = {}
    for i in record:
        a = i.split()
        code.append(a)
    for j in code:
        if j[0] == 'Enter' or j[0] == 'Change':
            online[j[1]] =j[2]
        
    for k in code:
        if k[0] == 'Enter':    
            answer.append("{0}님이 들어왔습니다.".format(online[k[1]]))
        if k[0] == 'Leave':
            answer.append("{0}님이 나갔습니다.".format(online[k[1]]))
        
    
    return answer