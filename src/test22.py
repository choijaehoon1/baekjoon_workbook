import copy
from collections import deque
import sys

def bfs(x,y):
    visit[x][y] = 1
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M:
                if visit[nx][ny] == 0 and board[nx][ny] > 0:
                    visit[nx][ny] = 1
                    q.append([nx,ny])

def update(check):
    new_board = [[0]*M for _ in range(N)]
    for cx,cy in check:
        tmp = 0
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 0:
                    tmp += 1

        if board[cx][cy] - tmp > 0:
            new_board[cx][cy] = board[cx][cy] - tmp
        else:
            new_board[cx][cy] = 0
    return new_board

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int, sys.stdin.readline().rstrip().split())

board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
time = 0
while True:    
    cnt = 0
    visit = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and visit[i][j] == 0:
                cnt += 1
                bfs(i,j)
    if cnt == 0:
        print(0)
        break                
    if cnt >= 2:
        print(time)
        break
    check = []
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                check.append([i,j])
    board = update(check) 
    time += 1
