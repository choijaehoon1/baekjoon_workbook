from collections import deque
import sys

def bfs(x):
    visit[x] = 1
    cnt = 1
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()        
        for i in board[x]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)

    return cnt

N,M = map(int,sys.stdin.readline().rstrip().split())
board = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    board[b].append(a)

table = []
for i in range(1,N+1):
    visit = [0 for _ in range(N+1)] 
    result = bfs(i)
    table.append([result,i])

table.sort(key = lambda x:(-x[0],x[1]))

max_value = 0
for t in table:
    if max_value < t[0]:
        max_value = t[0]
        result = [t[1]]
    elif max_value == t[0]:
        result.append(t[1])
print(*result)

