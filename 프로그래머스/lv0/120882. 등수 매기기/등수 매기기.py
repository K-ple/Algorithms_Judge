def solution(score):
    answer = []
    a = []
    rank = []
    dic = {}
    for i in score:
        a.append(sum(i))
        rank.append(sum(i))
    rank.sort(reverse = True)
    
    for j in range(len(a)):
        
        if rank[j] not in dic:
            dic[rank[j]] = j+1
    return [dic[i] for i in a]

# MK-1
'''def solution(score):
    answer = []
    dic = {}
    a = []
    for i in score:
        a.append(sum(i)//2) 
        answer.append(sum(i)//2)
    for k in range(len(a)):
        if answer.count(-1) > len(answer):
            break
        if answer[answer.index(max(answer))] not in dic:
            dic[answer[answer.index(max(answer))]] = k+1
        answer[answer.index(max(answer))] = -1
    print(a, dic)
    return [dic[i] for i in a]
    '''