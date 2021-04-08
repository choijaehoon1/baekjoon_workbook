from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y,0]) # 시작은 주어진 값이 항상 0이므로 벽을 안뚫은 경우
    dist[x][y][0] = 1

    while q:
        x,y,z = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 1<=nx<=N and 1<=ny<=M:
                # 이동가능한 칸이고 방문하지 않은 칸인경우
                if board[nx][ny] == 0 and dist[nx][ny][z] == -1:
                    dist[nx][ny][z] = dist[x][y][z] + 1
                    q.append([nx,ny,z])
                # 벽을 아직 뚫고오지 않았고 벽인칸이고 방문하지 않은 경우                    
                elif z == 0 and board[nx][ny] == 1 and dist[nx][ny][z] == -1:
                    dist[nx][ny][1] = dist[x][y][0] + 1 
                    q.append([nx,ny,1])

dx = [-1,1,0,0]
dy = [0,0,-1,1]    
board = [[]]
N,M = map(int,sys.stdin.readline().rstrip().split())
for i in range(N):
    board.append([-1] + list(map(int,sys.stdin.readline().rstrip())))
# 0번째 값에는 안뚫고 최단거리, 1번째 값에는 뚫고 최단거리의 값 저장
dist = [[[-1]*2 for _ in range(M+1)] for _ in range(N+1)]
bfs(1,1)
# cnt01 벽을 한번도 안뚫은 경우, cnt02 벽을 한번 뚫은 경우
cnt01,cnt02 = dist[N][M][0],dist[N][M][1]

if cnt01 == -1 and cnt02 != -1:
    print(cnt02)
elif cnt01 != -1 and cnt02 == -1:    
    print(cnt01)
else:
    print(min(cnt01,cnt02))
