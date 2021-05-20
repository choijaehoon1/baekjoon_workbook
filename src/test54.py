from collections import deque
import sys

def find():
    q = deque()
    q.append(N)
    dist[N] = 0
    visit[N] = 1

    while q:
        x = q.popleft()
        if 2*x < max_value and visit[2*x] == 0:
            visit[2*x] = 1
            dist[2*x] = dist[x]
            q.appendleft(2*x)

        if x+1 < max_value and visit[x+1] == 0:
            visit[x+1] = 1
            dist[x+1] = dist[x] + 1
            q.append(x+1)        

        if 0 <= x-1 and visit[x-1] == 0:
            visit[x-1] = 1
            dist[x-1] = dist[x] + 1
            q.append(x-1)

N,K = map(int,sys.stdin.readline().rstrip().split())
visit = [0 for _ in range(1000001)]
dist = [-1 for _ in range(1000001)]
max_value = 1000001
find()
print(dist[K])
