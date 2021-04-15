from collections import deque
import sys

def bfs(x):
    dist = [-1 for _ in range(N+1)]
    q = deque()
    q.append(x)
    dist[x] = 0
    while q:
        x = q.popleft()
        for i in board[x]:
            if dist[i] == -1:
                dist[i] = dist[x] + 1
                q.append(i)
    return sum(dist[1:])
      
N,M = map(int, sys.stdin.readline().rstrip().split())

board = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    board[a].append(b)
    board[b].append(a)

table = [0 for _ in range(N+1)]

for i in range(1,N+1):
    table[i] = bfs(i)

min_value = int(1e9)
for i in range(1,N+1):
    if min_value > table[i]:
        min_value = table[i]
        result = [i]
    elif min_value == table[i]:
        result.append(i) 
if len(result) == 1:
    print(*result)
if len(result) > 1:
    print(result[0])

