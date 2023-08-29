def solution(q, r, code):
    index = 0
    for i in range(21):
        if i % q == r:
            index = i
            break
    
    return code[index::q]