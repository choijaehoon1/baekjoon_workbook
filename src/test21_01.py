# 시간초과
from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    dist = [[INF]*(M+1) for _ in range(N+1)]
    dist[x][y] = 1

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 1<=nx<=N and 1<=ny<=M:
                if dist[nx][ny] == INF and board[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
    return dist

dx = [-1,1,0,0]
dy = [0,0,-1,1]    
board = [[]]
check = []
INF = int(1e9)
N,M = map(int,sys.stdin.readline().rstrip().split())
for i in range(N):
    board.append([-1] + list(map(int,sys.stdin.readline().rstrip())))

for i in range(1,N+1):
    for j in range(1,M+1):
        if board[i][j] == 1:
            check.append([i,j])

start_dist = bfs(1,1)
answer = start_dist[N][M]

for t in range(len(check)):
    x,y = check[t]
    board[x][y] = 0
    tmp_dist = bfs(1,1)
    if tmp_dist[N][M] != -1:
        answer = min(answer, tmp_dist[N][M])
    board[x][y] = 1

if answer == INF:
    print(-1)
else:
    print(answer)    
