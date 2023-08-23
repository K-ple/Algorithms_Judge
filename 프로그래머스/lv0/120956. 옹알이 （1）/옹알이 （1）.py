def solution(babbling):
    answer = 0
    check = ["aya","ye","woo","ma"]
    for i in babbling:
        count = 0
        while i:
            if count == 5:
                break
            for j in check:
                if i[:len(j)] == j:
                    i = i[len(j):]
            count += 1
        
        if not i:
            answer += 1
    return answer