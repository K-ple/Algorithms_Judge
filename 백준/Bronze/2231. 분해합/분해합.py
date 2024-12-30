n = int(input())
answer = []
for i in range(1, n):
    if i + sum([int(i) for i in str(i)]) == n:
        print(i)
        exit()
print(0)

    