def solution(sides):
    answer = 0
    a = max(sides)
    sides.remove(max(sides))
    if  a < sum(i for i in sides):
        return 1

    else:
        return 2