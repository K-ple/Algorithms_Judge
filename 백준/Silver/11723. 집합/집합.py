import sys
num = int(sys.stdin.readline())
s = set()

for _ in range(num):
    d = sys.stdin.readline().strip()
    if d == 'all':
        s = set(range(1, 21))
    elif d == 'empty':
        s.clear()
    else:
        order, x = d.split()
        x = int(x)  
        if order == 'add':
            s.add(x)
        elif order == 'remove':
            s.discard(x) 
        elif order == 'check':
            print(1 if x in s else 0)
        elif order == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.add(x)
