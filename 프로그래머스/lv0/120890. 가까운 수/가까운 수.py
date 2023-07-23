def solution(array, n):
    array.append(n)
    array = sorted(array)
    ix = array.index(n)
    if array.count(n) > 1:
            return n

    if array.index(n) != len(array)-1:
        

        if (array[ix-1] - n) * -1 <= array[ix+1] - n:
            return array[ix-1]
        else:
            return array[ix+1]
    else:
        return array[ix-1]  