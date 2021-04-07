import sys
from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    visit[node] = 1

    while q:
        x = q.popleft()
        for i in board[x]:
            if visit[i] == 0:
                dp[i] = x
                visit[i] = 1
                q.append(i)


N = int(sys.stdin.readline().rstrip())
board = [[] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    board[a].append(b)
    board[b].append(a)

bfs(1)
for i in range(2,len(dp)):
    print(dp[i])

