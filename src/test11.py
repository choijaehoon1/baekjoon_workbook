from itertools import combinations
from collections import deque
import copy
import sys

def bfs():
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x 
            ny = dy[k] + y
            if 0<=nx<N and 0<=ny<M:
                if visit[nx][ny] == 0 and new_board[nx][ny] == 0:
                    new_board[nx][ny] = 2
                    visit[nx][ny] = 1
                    q.append([nx,ny])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

board = []
wall_check = []
N,M= map(int, sys.stdin.readline().rstrip().split())
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(M):
        if board[i][j] == 0:
            wall_check.append([i,j])

answer = 0
for combi in list(combinations(wall_check,3)):
    visit = [[0]*M for _ in range(N)]
    new_board = copy.deepcopy(board)
    for cx,cy in combi:
        new_board[cx][cy] = 1

    q = deque()
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 2 and visit[i][j] == 0:
                visit[i][j] = 1
                q.append([i,j])

    bfs()        
    
    cnt = 0
    for i in range(N):
        cnt += new_board[i].count(0)
    answer = max(answer,cnt)

print(answer)
