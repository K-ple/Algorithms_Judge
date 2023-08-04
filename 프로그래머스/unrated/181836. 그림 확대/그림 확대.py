def solution(picture, k):
    answer = []
    for i in picture:
        reset = []
        for j in i:
            reset.append(j*k)
        for l in range(k):
            
            answer.append(''.join(reset))
    return answer