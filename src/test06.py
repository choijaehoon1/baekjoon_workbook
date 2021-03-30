from collections import deque
import sys

def bfs(x,y,cnt):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<N and 0<=ny<M:
                if visit[nx][ny] == 0 and board[nx][ny] == -1:
                    visit[nx][ny] = 1
                    board[nx][ny] = cnt
                    q.append([nx,ny])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    M,N,K = map(int, sys.stdin.readline().rstrip().split())
    board = [[0]*M for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    for i in range(K):
        X,Y = map(int, sys.stdin.readline().rstrip().split())
        board[Y][X] = -1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == -1:
                cnt += 1
                bfs(i,j,cnt)
    print(cnt)            
