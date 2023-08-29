def solution(arr):
    a = len(arr)
    b = len(arr[0])
    if a == b:
        pass
    elif a > b:
        for i in arr:
            for k in range(a-b):
                i.append(0)
    else:
        for j in range(b-a):
            arr.append([0]*b)
    return arr