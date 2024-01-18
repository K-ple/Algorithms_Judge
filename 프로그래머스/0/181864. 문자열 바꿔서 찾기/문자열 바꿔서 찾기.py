def solution(myString, pat):
    rp = ''
    for i in myString:
        if i == 'A':
            rp += 'B'
        else:
            rp += 'A'
    if pat in rp:
        return 1
    else:
        return 0
 