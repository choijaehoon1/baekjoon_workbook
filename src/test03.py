from collections import deque

def bfs(x,y):
    dist = [[-1]*(M+1) for _ in range(N+1)]
    q = deque()
    q.append([x,y])
    dist[x][y] = 1

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 1<=nx<N+1 and 1<=ny<M+1 and dist[nx][ny] == -1 and board[nx][ny] == 1: 
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])
    return dist

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int, input().split())
board = [[]]
for i in range(N):
    board.append([0] + list(map(int,input())))

result = bfs(1,1)
print(result[N][M])

