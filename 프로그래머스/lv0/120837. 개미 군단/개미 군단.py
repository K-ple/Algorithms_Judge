def solution(hp):
    answer = 0
    while True:
        if hp == 0:
            return answer
        elif hp >= 5:
            answer += hp // 5
            hp = hp%5
        elif 5> hp >= 3:
            answer += hp // 3
            hp = hp%3
        elif 0 < hp <3:
            answer += hp
            hp = 0
            
    