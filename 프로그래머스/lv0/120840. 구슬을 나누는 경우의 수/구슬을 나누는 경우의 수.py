def solution(balls, share):
    
    a = 1
    b = 1
    for i in range(share):
        a *= balls
        balls -=1
    for j in range(share):
        b *= share
        share -= 1
    return a / b