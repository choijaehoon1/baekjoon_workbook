from collections import deque
import sys

def check():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                return True
    return False

def bfs():
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 0 and visit[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    visit[nx][ny] = 1
                    q.append([nx,ny])
 
def proper():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and visit[i][j] == 0:
                return False
    return True                 

M,N = map(int, sys.stdin.readline().rstrip().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
visit = [[0]*M for _ in range(N)]
dist = [[-1]*M for _ in range(N)]

answer = 0
while True:
    if check():
        q = deque()
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1 and visit[i][j] == 0:
                    q.append([i,j])
        
        for x,y in q:
            visit[x][y] = 1
            dist[x][y] = 0

        bfs()            

        if proper() == False:
            print(-1)
            break
        else:
            max_value = 0
            for i in range(N):
                max_value = max(max_value,max(dist[i]))
            print(max_value)                
            break
    else:
        print(answer)
        break   

