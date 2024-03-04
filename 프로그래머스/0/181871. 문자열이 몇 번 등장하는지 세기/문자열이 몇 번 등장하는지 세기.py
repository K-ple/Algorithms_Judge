def solution(myString, pat):
    answer = 0
    length= len(pat)
    for i in range(len(myString)):
        if myString[i:i+length] == pat:
            answer += 1
    return answer