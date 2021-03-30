from collections import deque
import sys

def bfs(x):
    global result
    visit[x] = 1
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for i in range(1,n+1):
            if board[x][i] == 1 and visit[i] == 0:
                visit[i] = 1
                result += 1
                q.append(i)
                
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

board = [[0]*(n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    board[a][b] = 1
    board[b][a] = 1
result = 0
bfs(1)    
print(result)
