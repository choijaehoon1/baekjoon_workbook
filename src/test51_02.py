import sys
sys.setrecursionlimit(10**6)
def s_dfs(node):
    global short
    visit[node] = 1
    
    for i in board01[node]:
        if visit[i] == 0:
            short += 1
            s_dfs(i)
    return short            

def t_dfs(node):
    global tall
    visit[node] = 1
    
    for i in board02[node]:
        if visit[i] == 0:
            tall += 1
            t_dfs(i)
    return tall            


N,M = map(int,sys.stdin.readline().rstrip().split())
board01 = [[] for _ in range(N+1)]
board02 = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    board01[a].append(b)
    board02[b].append(a)
    
answer = 0
for i in range(1,N+1):
    short = 0
    tall = 0
    visit = [0 for _ in range(N+1)]
    s_dfs(i)
    visit = [0 for _ in range(N+1)]
    t_dfs(i)
    if short + tall == N-1:
        answer +=1 
print(answer)
