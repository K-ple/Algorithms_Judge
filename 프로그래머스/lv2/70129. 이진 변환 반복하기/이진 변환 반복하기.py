def solution(s):
    count = 0
    si = 0
    while s != '1':
        si += 1
        count += s.count('0')
        s = s.replace('0','')
        s = str(bin(len(s)))[2:]
        
        
    return [si,count]