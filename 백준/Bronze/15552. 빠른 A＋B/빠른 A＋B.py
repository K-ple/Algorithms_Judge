import sys
line = []
b = int(input())
for i in range(b):
    line.append(sys.stdin.readline())

for j in line:
    print(sum(map(int, j.split())))