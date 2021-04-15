from collections import deque
import sys

def bfs(x,flag):
    dist = [-1 for _ in range(V+1)]
    q = deque()
    q.append(x)
    dist[x] = 0

    while q:
        x = q.popleft()
        for i in board[x]:
            if dist[i[0]] == -1:
                dist[i[0]] = dist[x] + i[1]
                q.append(i[0]) 
        
    if flag == False:
        max_value = max(dist[1:])
        idx = dist.index(max_value)
        return idx
    else:
        return max(dist[1:])


V = int(sys.stdin.readline().rstrip())
board = [[] for _ in range(V+1)]
for i in range(V):
    tmp = list(map(int,sys.stdin.readline().rstrip().split()))
    a = tmp[0]
    tmp = tmp[1:-1]
    for j in range(0,len(tmp)-1,2):
        board[a].append([tmp[j],tmp[j+1]])

idx = bfs(1,False)
result = bfs(idx,True)
print(result)

