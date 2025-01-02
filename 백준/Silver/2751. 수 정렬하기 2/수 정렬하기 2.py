import sys
t = int(input())

answer = []
for i in range(t):
    answer.append(int(sys.stdin.readline()))
answer.sort()

for j in answer:
    print(j)
