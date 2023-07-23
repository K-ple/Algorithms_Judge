def solution(my_string):
    a = ''
    for i in my_string:
        if not i.isdigit():
            a += ' '
        else:
            a += i
    return sum(map(int,a.split()))