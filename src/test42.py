from collections import deque
import sys
def bfs(x):
    dist[x] = 0
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for k in range(2):
            nx = x + direc[k]
            if 1<=nx<=F and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    return
    
F,S,G,U,D = map(int,sys.stdin.readline().rstrip().split())
dist = [-1 for _ in range(F+1)]
direc = [U,-D]
bfs(S)
if dist[G] == -1:
    print('use the stairs')
else:
    print(dist[G])
