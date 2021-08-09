import sys
import heapq

N = int(sys.stdin.readline().rstrip())
h = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    
    if num != 0:
        heapq.heappush(h,[abs(num),num])
    else:
        if h:
            a,b = heapq.heappop(h)
            print(b)
        else:
            print(0)                    

