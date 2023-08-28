def solution(start, end_num):
    if start > end_num:
        return [i for i in range(start,end_num-1,-1)]
    elif start < end_num:
        return [i for i in range(start,end_num+1)]
    else:
        return start