import sys
import heapq as hq
count = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(count):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if heap:
            print(-hq.heappop(heap))
        else:
            print(0)
    else:
        hq.heappush(heap, -x)
    
    