def solution(my_string):
    li = my_string.split()
    answer = int(li[0])
    for i in range((len(li)-1)//2):
        if li[1+2*i] == '+':
            answer += int(li[2 + 2*i])
        else:
            answer -= int(li[2 + 2*i])
    return answer