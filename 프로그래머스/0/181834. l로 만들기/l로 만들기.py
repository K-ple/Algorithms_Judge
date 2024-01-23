def solution(myString):
    lowl = ['a','b','c','d','e','f','g','h','i','j','k']
    answer = ''
    for i in myString:
        if i in lowl:
            answer += 'l'
        else:
            answer += i
    return answer