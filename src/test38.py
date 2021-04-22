import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global answer
    global cycle

    if not (0<=x<N and 0<=y<M) or board[x][y] == 'H':
        return 0

    if visit[x][y] == 1:
        cycle = True
        return -1       
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    visit[x][y] = 1
    num = int(board[x][y])
    for k in range(4):
        nx = x + num*dx[k]
        ny = y + num*dy[k]

        dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)
        if cycle == True:
            return -1
    visit[x][y] = 0     
    return dp[x][y]       

cycle = False
answer = 0
N,M = map(int, sys.stdin.readline().rstrip().split())
board = []
for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

visit = [[0]*M for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

dfs(0,0)
if cycle == True:
    print(-1)
else:
    print(max(max(dp)))

