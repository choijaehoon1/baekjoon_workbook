import sys
from collections import deque
def bfs(node):
    q = deque()
    q.append(node)
    dist[node] = 0

    while q:
        x = q.popleft()
        for i in board[x]:
            if dist[i] == -1:
                dist[i] = dist[x] + 1
                q.append(i) 

n = int(sys.stdin.readline().rstrip())
man_01, man_02 = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
board = [[] for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]
for i in range(m):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    board[x].append(y)
    board[y].append(x)

bfs(man_01)

if dist[man_02] == -1:
    print(-1)
else:
    print(dist[man_02])    
