def solution(arr):
    num = len(arr)
    for i in range(num):
        for j in range(num):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1