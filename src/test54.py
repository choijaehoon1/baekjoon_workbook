from collections import deque
import sys

def dfs(node,depth):
    global flag
    if depth >= 4:
        flag = True
        return
    
    visit[node] = 1
    for i in board[node]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i,depth+1)
            visit[i] = 0 


N,M = map(int,sys.stdin.readline().rstrip().split())
board = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    board[a].append(b)
    board[b].append(a)

flag = False
for i in range(N):
    visit = [0 for _ in range(N)]
    dfs(i,0)
    if flag == True:
        break

if flag:
    print(1)
else:
    print(0)    

