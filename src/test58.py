# 위상정렬(사이클없고 방향만 존재하는 그래프에서 정점을 나열)
import heapq
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
result = []

h = []

for i in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1,N+1):
    if indegree[i] == 0:
        heapq.heappush(h,i)

while h:
    node = heapq.heappop(h)
    result.append(node)

    for i in graph[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(h,i)

print(*result)            


