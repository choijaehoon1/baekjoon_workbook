# dp는 값이 어떻다고 한 번 결정을 했으면 그 후로는 절대로 바뀌는 일이 없어야 합니다.
# 이미 어떤 좌표로부터 탐색을 끝낸 적이 있음에도 불구하고, 
# 값이 갱신되는 순간 똑같은 탐색을 또다시 반복해야 합니다. 
# 똑같은 탐색을 두 번 이상 반복할 필요가 없다.

import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    # dp의 값이 존재하면 이미 check한 값임(반복 체크하지 않겠다는 뜻)
    if dp[x][y]: # 값이 0이 아니면 리턴(1보다 크거나 같은 값)
        return dp[x][y]

    dp[x][y] = 1 # dfs타고 한번 방문하게 되면 dp값을 1로 초기화

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n:
            if board[x][y] < board[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx,ny) + 1)
    return dp[x][y]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(sys.stdin.readline().rstrip())
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0]*n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        # ex) 0행 2열의 경우 앞서 0행 1열의 dfs 수행할때 체크된 값으로 dp값이 변경되어있으므로
        # dfs 호출시 바로 저장되어있는 dp[x][y]값 리턴
        answer = max(answer, dfs(i,j))
print(answer)
