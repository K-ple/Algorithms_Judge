def solution(n, k):
    answer = ''
    m = {3:12, 4:9, 5:8, 6:7, 7:7, 8:6,9:6,10:5}
    for i in range(m[k],-1,-1):
        if n // k**i != 0:
            answer += str(n // k**i)
            n %= k**i
        elif answer:
            answer += '0'
    count = 0
    answer = answer.split('0')
    
    for j in answer:
        if j == '1' or j =='':
            continue
        k = int(j)
        for l in range(2,int(k**0.5)+1):
            if k % l == 0:
                count -= 1
                break
        count += 1
    return count