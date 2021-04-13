from collections import deque
import sys

def bfs(x,flag):
    dist = [-1 for _ in range(n+1)]
    dist[x] = 0
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for i,w in board[x]:
            if dist[i] == -1:
                dist[i] = dist[x] + w
                q.append(i)
    if flag == False:
        idx = dist.index(max(dist[1:]))
        return idx
    else:
        max_value = max(dist[1:])
        return max_value

n = int(sys.stdin.readline().rstrip())
board = [[] for _ in range(n+1)]

for i in range(n-1):
    p,c,w = map(int, sys.stdin.readline().rstrip().split())
    board[p].append([c,w])
    board[c].append([p,w])
    
result = 0
idx = bfs(1,False)
print(bfs(idx,True))


