# 메모리 초과
from collections import deque
import sys

def bfs(x,flag):
    dist = [-1 for _ in range(V+1)]
    q = deque()
    q.append(x)
    dist[x] = 0

    while q:
        x = q.popleft()
        for i in range(1,V+1):
            if board[x][i] != 0 and dist[i] == -1:
                dist[i] = dist[x] + board[x][i]
                q.append(i)

    if flag == False:
        max_value = max(dist[1:])
        idx = dist.index(max_value)
        return idx
    else:
        return max(dist[1:])


V = int(sys.stdin.readline().rstrip())
board = [[0]*(V+1) for _ in range(V+1)]

for i in range(V):
    tmp = list(map(int,sys.stdin.readline().rstrip().split()))
    a = tmp[0]
    tmp = tmp[1:-1]
    for j in range(0,len(tmp)-1,2):
        board[a][tmp[j]] = tmp[j+1]

idx = bfs(1,False)
result = bfs(idx,True)
print(result)

