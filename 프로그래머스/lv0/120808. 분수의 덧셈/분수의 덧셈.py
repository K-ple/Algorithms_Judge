def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1 * denom2 +numer2 * denom1
    dc = []
    nc = []
    for i in range(1,denom+1):
        if denom % i == 0:
            dc.append(i)
    for j in range(1,numer+1):
        if numer % j == 0:
            nc.append(j)
    for k in range(1,len(nc)+1):
        if nc[-k] in dc:
            if denom // nc[-k] >= 1 and numer // nc[-k] >= 1 and denom % nc[-k] == 0 and numer % nc[-k] == 0:
                denom = denom / nc[-k]
                numer = numer / nc[-k]

    return [numer, denom]