def solution(dots):
    a,b,c,d = dots


    if abs(a[0]-b[0]) == abs(c[0]-d[0]) and abs(a[1]-b[1]) == abs(c[1]-d[1]):
        return 1
        
    if abs(a[0]-c[0]) == abs(b[0]-d[0]) and abs(a[1]-c[1]) == abs(b[1]-d[1]):
        return 1
    
    if abs(a[0]-d[0]) == abs(c[0]-b[0]) and abs(a[1]-d[1]) == abs(c[1]-b[1]):
        return 1
    if (b[0] - a[0]) * (d[1] - c[1]) == (d[0] - c[0]) * (b[1] - a[1]):
        return 1
            
    return 0