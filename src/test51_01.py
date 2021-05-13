import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
INF = int(1e9)
board = [[INF]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    board[a][b] = 1
    
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            board[i][j] = 0

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            if board[a][k] + board[k][b] == 2:
                board[a][b] = 1

cnt = [0]*(N+1)
for i in range(1,N+1):
    for j in range(1,N+1):
        if board[i][j] == 1:
            cnt[i] += 1
            cnt[j] += 1
         
answer = 0
for i in cnt:
    if i == N-1:
        answer += 1
print(answer)         

