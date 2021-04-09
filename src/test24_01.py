# 시간초과(dp적용이 필요)
import sys

def dfs(x,y,cnt,current):
    global answer
    visit[x][y] = 1
    answer = max(answer,cnt)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n:
            if visit[nx][ny] == 0 and current < board[nx][ny]:
                visit[nx][ny] = 1
                dfs(nx,ny,cnt+1,board[nx][ny])
                visit[nx][ny] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(sys.stdin.readline().rstrip())
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [0]*(n*n)
cnt = -1
for i in range(n):
    for j in range(n):
        visit = [[0]*n for _ in range(n)]
        answer = 0
        dfs(i,j,1,board[i][j])
        cnt += 1
        dp[cnt] = answer
print(max(dp))
