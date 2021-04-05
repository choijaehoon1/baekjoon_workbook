import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 0
def dfs(x,y,cnt):
    global answer
    visit[x][y] = 1
    answer = max(answer,cnt)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<R and 0<=ny<C:
            if visit[nx][ny] == 0 and alpha[ord(board[nx][ny])-ord('A')] == 0:
                visit[nx][ny] = 1
                alpha[ord(board[nx][ny])-ord('A')] = 1
                dfs(nx,ny,cnt+1) 
                visit[nx][ny] = 0
                alpha[ord(board[nx][ny])-ord('A')] = 0

R,C = map(int, sys.stdin.readline().rstrip().split())
board = []
for i in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

visit = [[0]*C for _ in range(R)]
alpha = [0]*26
alpha[ord(board[0][0])-ord('A')] = 1
dfs(0,0,1)
print(answer)    
