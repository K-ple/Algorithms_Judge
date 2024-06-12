def solution(bandage, health, attacks):
    answer = health
    time = 0
    h_time = 0
    a_time, a_damage = attacks.pop(0)
    end = attacks[-1][0]
    while end >= time:
        if a_time == time:
            answer -= a_damage
            h_time = 0
            try:
                a_time, a_damage = attacks.pop(0)
            except:
                break
        else:
            if answer < health:
                answer += bandage[1]
                h_time += 1
                if h_time == bandage[0]:
                    answer += bandage[2]
                    h_time = 0
        if answer > health:
            answer = health
        elif answer <= 0:
            return -1
        time += 1
    return answer if answer > 0 else -1