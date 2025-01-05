import sys
n, m = map(int, sys.stdin.readline().split())
password = {}
for i in range(n):
    site, p = sys.stdin.readline().split()
    password[site] = p

for _ in range(m):
    print(password[input()])