def solution(polynomial):
    answer = ''
    xname = 0
    dname = 0
    if polynomial == 'x':
        return 'x'
    polylist = polynomial.split(' + ')
    
    for i in polylist:
        
        if 'x' in i:
            if i == 'x':
                xname += 1
            else:
                xname += int(i[:-1])
        else:
            dname += int(i)

    if dname == 0:
        return '{}x'.format(xname)
    elif xname == 0:
        return str(dname)
    if xname == 1:
        return 'x + {}'.format(dname)
    return '{0}x + {1}'.format(xname, dname)