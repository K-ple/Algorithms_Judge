import sys
n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j +1, n):
            s = number[i] + number[j] + number[k]
            if s <= m:
                answer = max(answer, s)
                
print(answer)