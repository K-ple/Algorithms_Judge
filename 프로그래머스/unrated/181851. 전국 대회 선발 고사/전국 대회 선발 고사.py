def solution(rank, attendance):
    answer = 0
    r = []
    for i in range(1,len(rank)+1):
        if attendance[rank.index(i)]:
            r.append(rank.index(i))
        if len(r) == 3:
            return 10000*r[0]+100*r[1]+r[2]