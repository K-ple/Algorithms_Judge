def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += '{}{}'.format(str1[i], str2[i])
    return answer