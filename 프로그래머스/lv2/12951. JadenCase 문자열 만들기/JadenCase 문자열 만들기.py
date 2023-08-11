def solution(s):
    re = [s[0].upper()]
    for i in s[1:]:
        if re[-1] == ' ':
            if i == ' ':
                re.append(i)
            else:
                re.append(i.upper())
        else:
            re.append(i.lower())   
            
    return ''.join(re)