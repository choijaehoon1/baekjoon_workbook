from collections import deque
import sys

def bfs(x):
    visit[x] = 1
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for i in range(1,N+1):
            if graph[x][i] == 1 and visit[i] == 0:
                visit[i] = 1
                q.append(i)

N,M = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    u,v = map(int, sys.stdin.readline().rstrip().split())
    graph[u][v] = 1
    graph[v][u] = 1

visit = [0 for _ in range(N+1)]

answer = 0
for i in range(1,N+1):
    if visit[i] == 0:
        answer += 1
        bfs(i)
print(answer)
