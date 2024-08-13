def change(time):
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

def solution(plans):
    answer = []
    stay = []
    time = 0
 
    for i in range(len(plans)):
        plans[i][1] = change(plans[i][1])
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    
    
    while True:            
        name, time, playtime = plans.pop(0)
        end_time = time + playtime
        
        if not plans:
            answer.append(name)
            break
        
        if plans[0][1] >= end_time:
            answer.append(name)
            time = end_time
            while stay:
                if plans[0][1] >= time + stay[0][1]:
                    name, playtime = stay.pop(0)
                    answer.append(name)
                    time += playtime
                else:
                    stay[0][1] -= plans[0][1] - time
                    break
        else:
            stay.insert(0,[name, end_time - plans[0][1]]) 
        
        
        
    for i in stay:
        answer.append(i[0])
    return answer
