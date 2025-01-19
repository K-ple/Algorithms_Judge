import sys
n, m = map(int, sys.stdin.readline().split())
poket = {}
num = 1
for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    poket[name] = num
    poket[str(num)] = name
    num += 1
    
for j in range(m):
    print(poket[sys.stdin.readline().rstrip()])
