def solution(emergency):
    em = sorted(emergency)[::-1]
    a = []
    for i in emergency:
        i = em.index(i)+1
        a.append(i)
    return a