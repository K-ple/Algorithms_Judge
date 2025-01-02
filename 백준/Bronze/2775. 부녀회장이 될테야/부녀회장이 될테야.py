t = int(input())

for i in range(t):
    floor = int(input())
    room = int(input())
    apt = [[j for j in range(1, room+1)]]
    for _ in range(floor):
        
        f = []
        for j in range(room):
            f.append(sum(apt[-1][:j+1]))
            
        apt.append(f)
            
    print(apt[-1][room-1])
    