def solution(arr):
    answer = 0
    c = [arr]
    while True:
        answer += 1
        check = []
        for i in c[-1]:
            if i > 50 and i % 2 == 0:
                check.append(i//2)
            elif i < 50 and i % 2 != 0:
                check.append((i*2)+1)
            else:
                check.append(i)
        if c[-1] == check:
            return answer - 1
        
        c.append(check)