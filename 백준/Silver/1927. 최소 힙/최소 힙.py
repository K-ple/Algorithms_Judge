import sys
import heapq
num = int(sys.stdin.readline().rstrip())
h = []

for _ in range(num):
    m = int(sys.stdin.readline().rstrip())
    
    if m:
        heapq.heappush(h,m)
    else:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
