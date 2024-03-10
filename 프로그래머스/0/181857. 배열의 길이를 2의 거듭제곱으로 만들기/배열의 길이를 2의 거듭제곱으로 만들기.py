def solution(arr):
    if len(arr) == 1:
        return arr
    two = 2
    while len(arr) > two:
        two *= 2
    if two == len(arr):
        return arr
    for i in range(two-len(arr)):
        arr.append(0)
    return arr