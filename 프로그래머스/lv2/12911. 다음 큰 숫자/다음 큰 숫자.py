def solution(n):

    e = str(bin(n))[2:]
    num = int(e,2)
    if e.count('1') == len(e):
        return int(''.join(['10',e[1:]]),2)
    else:
        while True:
            num += 1
            if str(bin(num))[2:].count('1') == e.count('1'):
                return num