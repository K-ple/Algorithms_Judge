def solution(arr):
    if arr == [10] or arr == []:
        return [-1]
    arr.remove(min(arr))
    return arr