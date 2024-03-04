def solution(myString, pat):
    answer = ''
    reverse_string = myString[::-1]
    reverse_pat = pat[::-1]
    for i in range(len(reverse_string)):
        if reverse_string[i:i+len(pat)] == reverse_pat:
            answer += reverse_string[i:]
            break
    return answer[::-1]