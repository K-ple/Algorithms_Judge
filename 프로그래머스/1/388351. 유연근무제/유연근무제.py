def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        s_day = startday
        s_hour = schedules[i]//100
        s_minute = schedules[i]%100
        s_minute += 10

        if s_minute >= 60:
            s_hour += 1
            s_minute -= 60


        for j in timelogs[i]:
            
            if s_day == 7:
                s_day = 1
                
            elif s_day == 6:
                
                s_day += 1
            elif s_hour*100 + s_minute >= j:
                
                s_day +=1
                continue
            else:
                answer -= 1
                break
        answer += 1
    return max([0,answer])