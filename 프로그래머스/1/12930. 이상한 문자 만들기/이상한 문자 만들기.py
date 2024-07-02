def solution(s):
    count = 0
    answer = ''
    for i in s:
        if i == ' ':
            count = 0
            answer += ' '
            continue
        elif count % 2 == 0:
            answer += i.upper()
        else:
            answer += i.lower()
        count += 1
    return answer