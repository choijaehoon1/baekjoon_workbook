from collections import deque
import sys

def bfs(x,y):
    dist = [[-1]*M for _ in range(N)]
    dist[x][y] = 0
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 'L' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
    tmp = 0
    for d in dist:
        tmp = max(tmp, max(d))
    return tmp


dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 0
N,M = map(int,sys.stdin.readline().rstrip().split())
board = []
for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            answer = max(answer,bfs(i,j))
print(answer)            

