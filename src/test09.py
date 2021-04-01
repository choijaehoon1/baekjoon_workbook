from collections import deque
import sys

N,K = map(int,sys.stdin.readline().rstrip().split())
dist = [-1 for _ in range(100001)]

q = deque()
q.append([N,0])
dist[N] = 0

while q:
    x,time = q.popleft()
    dist[x] = time
    if x == K:
        print(time)
        break

    if 0<=x-1<100001:
        if dist[x-1] == -1:
            q.append([x-1,time+1]) 
    if 0<=x+1<100001:            
        if dist[x+1] == -1:
            q.append([x+1,time+1]) 
    if 0<=2*x<100001:            
        if dist[2*x] == -1:
            q.append([2*x,time+1])

