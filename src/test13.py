from collections import deque
import sys

def exclude(x1,y1,x2,y2):
    for j in range(x1,x2):
        for i in range(y1,y2):
            board[i][j] = -1

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    tmp = 1

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<M and 0<=ny<N:
                if visit[nx][ny] == 0 and board[nx][ny] == 0:
                    visit[nx][ny] = -1
                    tmp += 1
                    q.append([nx,ny])
    answer.append(tmp)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

M,N,K = map(int, sys.stdin.readline().rstrip().split())
board = [[0]*N for _ in range(M)]
visit = [[0]*N for _ in range(M)]
for i in range(K):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().rstrip().split())
    exclude(x1,y1,x2,y2)

cnt = 0
answer = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and visit[i][j] == 0:
            cnt += 1
            bfs(i,j)
print(cnt)
answer.sort()
for i in answer:
    print(i, end = ' ')

