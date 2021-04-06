import sys

def dfs(node):
    for i in board[node]:
        if visit[i] == 0:
            visit[i] = visit[node] + 1
            dfs(i)        

n = int(sys.stdin.readline().rstrip())
man_01, man_02 = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
board = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for i in range(m):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    board[x].append(y)
    board[y].append(x)

dfs(man_01)

if visit[man_02] == 0:
    print(-1)
else:
    print(visit[man_02])    
