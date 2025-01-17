import sys
people = int(sys.stdin.readline())
size = [int(i) for i in input().split()]
t, p = map(int, sys.stdin.readline().split())

s = 0
for i in size:
    if i % t == 0:
        s += i//t
    else:
        s += (i//t) + 1
print(s)
print(people//p, people%p)