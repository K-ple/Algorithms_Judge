def solution(friends, gifts):
    answer = []
    
    gift_point = {i:0 for i in friends}
    ft = {i:[0]*len(friends) for i in friends}
    
    none_count = 0
    for f in friends:
        ft[f][none_count] = -1
        none_count +=1
    
    for g in gifts:
        fr, to = g.split()
        gift_point[fr] += 1
        gift_point[to] -= 1
        ft[fr][friends.index(to)] += 1    
    
    for i in friends:
        a = 0
        for j in range(len(friends)):
            if ft[i][j] != -1:
                if ft[i][j] > ft[friends[j]][friends.index(i)]:
                    a += 1
                elif ft[i][j] == ft[friends[j]][friends.index(i)] and gift_point[i] > gift_point[friends[j]]:               a += 1
            
        answer.append(a)
        
    return max(answer)