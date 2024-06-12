answer = 0
re = int(input())
num = map(int, input().split())
sosu = [[j for j in range(1, i+1) if i % j == 0] for i in num]
for i in sosu:
    if len(i) == 2:
        answer += 1
print(answer)
