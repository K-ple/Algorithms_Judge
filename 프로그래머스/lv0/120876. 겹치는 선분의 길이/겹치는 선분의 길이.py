def solution(lines):
    a = {i for i in range(lines[0][0],lines[0][1])}
    b = {i for i in range(lines[1][0],lines[1][1])}
    c = {i for i in range(lines[2][0],lines[2][1])}
    ab = a&b
    bc = b&c
    ac = a&c
    return len(ab|bc|ac)
    