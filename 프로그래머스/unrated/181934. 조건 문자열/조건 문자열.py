def solution(ineq, eq, n, m):
    answer = 0
    if eq == "=":
        if ineq ==">":
            answer = n>=m
        elif ineq =="<":
            answer = n<=m
    elif eq == "!":
        if ineq ==">":
            answer = n>m
        elif ineq =="<":
            answer = n<m
    return int(answer)