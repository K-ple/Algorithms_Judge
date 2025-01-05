import sys
answer = 0
n, k = map(int, sys.stdin.readline().split())
money = []
for i in range(n):
    money.append(int(sys.stdin.readline()))

    
money.sort(reverse=True)

for i in money:
    if k % i != k:
        answer += k//i
        k %= i
print(answer)
 