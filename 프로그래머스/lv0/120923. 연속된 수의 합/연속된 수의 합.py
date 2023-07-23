def solution(num, total):
    if num == 1 and total == 0:
        return [0]
    for i in range(-50,1002-num):
        n = 0
        check = [i + k for k in range(num)]
        if sum(check) == total:
            return check
    