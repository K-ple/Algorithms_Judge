d_list = []
b_list = []
d, b = map(int, input().split())
for i in range(d):
    d_list.append(input())

for i in range(b):
    b_list.append(input())
    
db = set(d_list)&set(b_list)

db = sorted(list(db))

print(len(db))
for i in db:
    print(i)
  