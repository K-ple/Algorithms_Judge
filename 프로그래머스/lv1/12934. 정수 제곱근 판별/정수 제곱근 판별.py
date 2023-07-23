def solution(n):
    z = n ** 0.5
    
    if int(z) == z:
        return (z+1)**2
    else:
        return -1