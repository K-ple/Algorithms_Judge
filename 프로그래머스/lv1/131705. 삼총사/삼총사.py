def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(1+i,len(number)-1):
            for k in range(1+j,len(number)):
                
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
                    
                
    return answer