def solution(keymap, targets):
    answer = []

    for i in targets:
        count = 0

        for j in i:
            idx = []
            for k in keymap:
                if j in k:
                    idx.append(k.index(j)+1)
                
            
            if not idx:
                count = -1
                break
            count += min(idx)
            
        answer.append(count)
    return answer
