def solution(numbers, k):
    a = []
    while len(a) < 2*k-1:  
        for i in numbers:
            a.append(i)
    a = a[::2]
    return a[k-1]