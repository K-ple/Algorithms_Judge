import sys
n = int(sys.stdin.readline())
a = {i : 1 for i in map(int, sys.stdin.readline().split())}


m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))


for i in b:
    try:
        a[i] +=1
    except:
        print(0)
    else:
        print(1)