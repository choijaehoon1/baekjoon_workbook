# 메모리 초과
from collections import deque
import sys

def island(x,y,cnt):
    visit[x][y] = 1
    q = deque()
    q.append([x,y])
    new_board[x][y] = cnt

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if visit[nx][ny] == 0 and board[nx][ny] == 1:
                    visit[nx][ny] = 1
                    new_board[nx][ny] = cnt
                    q.append([nx,ny])

def issea(x,y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<N and 0<=ny<N and new_board[nx][ny] == 0:
            return True
    return False

def min_dist(c_x,c_y,dest_list):
    dist = [[-1]*N for _ in range(N)]
    dist[c_x][c_y] = 0
    q = deque()
    q.append([c_x,c_y]) 
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
    
    num = int(1e9)
    for d_x,d_y in dest_list:
        num = min(num,dist[d_x][d_y]-1)

    return num

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(sys.stdin.readline().rstrip())
new_board = [[0]*N for _ in range(N)]
visit = [[0]*N for _ in range(N)]
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))


cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visit[i][j] == 0:
            cnt += 1
            island(i,j,cnt)
      
check_list = []
dest_list = []
for i in range(N):
    for j in range(N):
        for k in range(1,cnt+1):
            if new_board[i][j] == k:
                if issea(i,j):
                    check_list.append([i,j,k])
            if new_board[i][j] != k and new_board[i][j] != 0:
                if issea(i,j):
                    dest_list.append([i,j,k])

answer = int(1e9)
for k in range(1,cnt+1):
    new_check = []
    new_dest = []
    for check in check_list:
        x,y,c = check
        if c == k:
            new_check.append([x,y])
    
    for dest in dest_list:
        x,y,c = dest
        if c == k:
            new_dest.append([x,y])

    for c_x,c_y in new_check:
        tmp = min_dist(c_x,c_y,new_dest)
    answer = min(answer,tmp)    

print(answer)            

