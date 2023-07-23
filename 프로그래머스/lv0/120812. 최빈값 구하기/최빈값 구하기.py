def solution(array):
    answer = 0
    a = 0
    b = 0
    for i in array:
        if answer == None:
            a = i
            
        elif array.count(a) < array.count(i):
            b = 0
            a = i
            
        elif a != i:
            if array.count(a) == array.count(i):
                b = 1
                a = i
                
    if b == 1:
        return -1
    return a