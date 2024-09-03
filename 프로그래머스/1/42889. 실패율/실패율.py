def solution(N, stages):
    st = {stage:0 for stage in range(1, N+1)}
    max_people = len(stages)
    
    for i in range(1,N+1):
        
            
        num = 0
        for j in stages:
            if j > i:
                num += 1
        
        st[i] = (max_people-num) / max_people
        max_people -= max_people - num

        if max_people <= 0:
            break
        
    answer = sorted(st.items(),key=lambda x: [x[1],-x[0]],reverse=True)
    return [i[0] for i in answer]