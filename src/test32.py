import sys

def dfs(x):
    global answer
    flag = False # leaf노드인 경우는 타고 내려갈 것이 없으므로 flag 값 안변함            

    visit[x] = 1
    for i in range(N):
        if board[x][i] == 1 and visit[i] == 0:
            flag = True
            dfs(i)
    if flag == False:
        answer += 1

N = int(sys.stdin.readline().rstrip())
board = [[0]*N for _ in range(N)]
nodes = list(map(int, sys.stdin.readline().rstrip().split()))
D = int(sys.stdin.readline().rstrip())
for i in range(len(nodes)):
    if nodes[i] != -1:
        board[i][nodes[i]] = 1
        board[nodes[i]][i] = 1
    else:
        root = i

for i in range(N):
    board[D][i] = 0
    board[i][D] = 0

answer = 0
visit = [0 for _ in range(N)]
dfs(root)
if D == root:
    print(0)
else:
    print(answer)        

