from collections import deque
def bfs(V):
    q = deque()
    q.append(V)
    visit[V] = 1
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(1,N+1):
            if board[x][i] == 1 and visit[i] == 0:
                visit[i] = 1
                q.append(i)
                    
N,M,V = map(int, input().split())
board = [[0]*(N+1) for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1

bfs(V)
