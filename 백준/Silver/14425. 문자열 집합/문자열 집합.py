n, m = map(int,input().split())
model = []
count = 0
for _ in range(n):
    model.append(input())

for _ in range(m):
    test = input()
    if test in model:
        count += 1
print(count)