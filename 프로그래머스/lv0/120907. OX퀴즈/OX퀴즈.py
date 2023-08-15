def solution(quiz):
    r = []
    for i in quiz:
        answer = i.split()
        a = int(answer[0])
        b = int(answer[2])
        an = int(answer[4])
        yeon = answer[1]
        if yeon == '+':
            if a + b == an:
                r.append('O')
            else:
                r.append("X")
        else:
            if a - b == an:
                r.append('O')
            else:
                r.append("X")
        
    return r