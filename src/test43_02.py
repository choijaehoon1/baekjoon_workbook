import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visit[node] = 1
    dp[node][0] = 0
    dp[node][1] = 1
    for i in board[node]:
        if visit[i] == 0:
            dfs(i)
            dp[node][0] += dp[i][1]
            dp[node][1] += min(dp[i][0],dp[i][1])
            
N = int(sys.stdin.readline().rstrip())
board = [[] for _ in range(N+1)]
dp = [[0,0] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    board[a].append(b)
    board[b].append(a)

dfs(1)
print(min(dp[1][0],dp[1][1]))

