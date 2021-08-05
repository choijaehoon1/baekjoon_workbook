import sys
import heapq

N = int(sys.stdin.readline().rstrip())
h = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heapq.heappush(h,-num)
    else:
        if h:
            answer = heapq.heappop(h)
            print(-answer)
        else:
            print(0)                    

