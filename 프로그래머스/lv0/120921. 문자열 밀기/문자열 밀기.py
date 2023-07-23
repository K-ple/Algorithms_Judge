def solution(A, B):
    if A == B:
        return 0
    count = 0
    
    while A != B:
        count += 1
        A = ''.join([A[-1],A[:len(A)-1]])
        if count == 100:
            return -1
    return count
        