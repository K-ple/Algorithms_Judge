def solution(arr, delete_list):
    for i in delete_list:
        if i in arr:
            ide = arr.index(i)
            arr.pop(ide)
            
    return arr