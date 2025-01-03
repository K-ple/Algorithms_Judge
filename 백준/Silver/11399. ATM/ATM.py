n = int(input())
s = [int(i) for i in input().split()]
s.sort()
answer = []
for i in range(1, n+1):
    answer.append(sum(s[:i]))
print(sum(answer))
    