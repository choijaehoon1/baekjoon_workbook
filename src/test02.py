def dfs(V):
    visit[V] = 1
    print(V, end=' ')
    for i in range(1,N+1):
        if board[V][i] == 1 and visit[i] == 0:
            dfs(i)

N,M,V = map(int, input().split())
board = [[0]*(N+1) for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1

dfs(V)
