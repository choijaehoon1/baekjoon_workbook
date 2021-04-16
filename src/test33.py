from collections import deque
import sys

def check(x,y):
    visit[x][y] = 1
    q = deque()
    q.append([x,y])
    tmp = []
    tmp.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == 0:
                if L<=abs(board[nx][ny]-board[x][y])<=R:
                    visit[nx][ny] = 1
                    tmp.append([nx,ny])
                    q.append([nx,ny])       
    return tmp                    

def bfs(possible_list):
    cnt = 0
    sum_value = 0
    for x,y in possible_list:
        sum_value += board[x][y]     
        cnt += 1
    avg_value = sum_value // cnt
    for x,y in possible_list:
        board[x][y] = avg_value

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,L,R = map(int,sys.stdin.readline().rstrip().split())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

answer = 0
while True:
    visit = [[0]*N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                possible_list = check(i,j)
                if len(possible_list) > 1:
                    flag = True
                    bfs(possible_list)
    if flag == False:
        print(answer)
        break
    answer += 1
