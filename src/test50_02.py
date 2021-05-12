from collections import deque
import sys

def island(x,y,cnt):
    visit[x][y] = 1
    q = deque()
    q.append([x,y])
    new_board[x][y] = cnt

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if visit[nx][ny] == 0 and board[nx][ny] == 1:
                    visit[nx][ny] = 1
                    new_board[nx][ny] = cnt
                    q.append([nx,ny])

def bfs(num):
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if new_board[nx][ny] != num and board[nx][ny] == 1:
                    return dist[x][y] # 가장 먼저 접하게 섬에 다른 섬에 도착했을 때 리턴 됨

                if dist[nx][ny] == -1 and board[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(sys.stdin.readline().rstrip())
new_board = [[0]*N for _ in range(N)]
visit = [[0]*N for _ in range(N)]
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))


cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visit[i][j] == 0:
            cnt += 1
            island(i,j,cnt)

# print(new_board)
answer = int(1e9)
for k in range(1,cnt+1):
    dist = [[-1]*N for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if new_board[i][j] == k and board[i][j] == 1:
                q.append([i,j])
                dist[i][j] = 0
    tmp = bfs(k)         
    answer = min(tmp,answer)
print(answer)    
