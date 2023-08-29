def solution(arr):

    if 2 not in arr:
        return [-1]
    if arr.count(2) == 1:
        return [2]
    
    revera = list(reversed(arr))
    rin = len(arr) - revera.index(2)
    oin = arr.index(2)
    return arr[oin:rin]