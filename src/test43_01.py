# 메모리 초과
import sys
sys.setrecursionlimit(10**9)

def dfs(node):
    visit[node] = 1

    for i in board[node]:
        if visit[i] == 0:
            sub[node].append(i)
            dfs(i)

def get_dp(node,flag):
    if flag:
        if dp[node][1] != -1:
            return dp[node][1]
        dp[node][1] = 1
        for i in sub[node]:
            dp[node][1] += min(get_dp(i,True),get_dp(i,False))
        return dp[node][1]
    else:
        if dp[node][0] != -1:
            return dp[node][0]
        dp[node][0] = 0
        for i in sub[node]:
            dp[node][0] += get_dp(i,True)
        return dp[node][0]                                        

N = int(sys.stdin.readline().rstrip())
board = [[] for _ in range(N+1)]
dp = [[-1,-1] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
sub = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    board[a].append(b)
    board[b].append(a)
dfs(1)
# print(sub)
print(min(get_dp(1,True), get_dp(1,False)))

