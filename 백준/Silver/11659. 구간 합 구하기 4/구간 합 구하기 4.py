import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

nujuck = [0] * (n+1)
for i in range(1,n+1):
    nujuck[i] = nujuck[i-1] + num[i - 1]

for _ in range(m):
    j, k = map(int, sys.stdin.readline().split())
    print(nujuck[k] - nujuck[j-1])