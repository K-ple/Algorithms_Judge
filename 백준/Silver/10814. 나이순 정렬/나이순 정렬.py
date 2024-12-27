n_a = []
num = int(input())
for i in range(num):
    age, name = input().split()
    n_a.append([int(age),name])

n_a = sorted(n_a, key=lambda x: x[0])

for a, n in n_a:
    print(a,n)
