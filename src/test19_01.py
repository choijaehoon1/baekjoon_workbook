import sys
sys.setrecursionlimit(10**9)

def dfs(node):
    visit[node] = 1
    for i in board[node]:
        if visit[i] == 0:
            dp[i] = node
            visit[i] = 1
            dfs(i)

N = int(sys.stdin.readline().rstrip())
board = [[] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    board[a].append(b)
    board[b].append(a)

dfs(1)
for i in range(2,len(dp)):
    print(dp[i])

