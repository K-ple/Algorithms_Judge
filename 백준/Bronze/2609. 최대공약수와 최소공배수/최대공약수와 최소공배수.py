a, b = map(int, input().split())
a_yak = []
b_yak = []
    
    
for i in range(1,a//2+1):
    if a % i == 0:
        a_yak.append(i)
for i in range(1, b//2+1):
    if b % i == 0:
        b_yak.append(i)
a_yak.append(a)
b_yak.append(b)

if a> b:
    a_yak.reverse()
    for i in a_yak:
        if i in b_yak:
            print(i)
            break
else:
    b_yak.reverse()
    for i in b_yak:
        if i in a_yak:
            print(i)
            break

        

a_bae = []
b_bae = []
z = 1
while True:
    a_bae.append(a*z)
    b_bae.append(b*z)
    if a*z in b_bae:
        print(a*z)
        break
    elif b*z in a_bae:
        print(b*z)
        break
    z += 1
    
        

