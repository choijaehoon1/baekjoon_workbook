import sys
import heapq

N = int(sys.stdin.readline().rstrip())
h = []

for i in range(N):
    tmp = list(map(int,sys.stdin.readline().rstrip().split()))

    if not h:
        for j in tmp:
            heapq.heappush(h,j)
    else:
        for j in tmp:
            if h[0] < j:
                heapq.heappush(h,j)
                heapq.heappop(h)     
print(h[0])                       

