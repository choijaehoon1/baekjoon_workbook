from collections import deque

def bfs(x,y,cnt):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    board[x][y] = cnt
    tmp = 1

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<N and 0<=ny<N:
                if visit[nx][ny] == 0 and board[nx][ny] == -1:
                    visit[nx][ny] = 1
                    board[nx][ny] = cnt
                    tmp += 1
                    q.append([nx,ny]) 
    return tmp

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
visit = [[0]*N for _ in range(N)]
board = []
for i in range(N):
    board.append(list(map(int,input())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            board[i][j] = -1

cnt = 0
answer = []
for i in range(N):
    for j in range(N):
        if board[i][j] == -1:
            cnt += 1
            tmp = bfs(i,j,cnt)
            answer.append(tmp)
            
answer.sort()
print(cnt)
for i in answer:
    print(i)

