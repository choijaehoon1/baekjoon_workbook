from collections import deque
import sys

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def bfs(x,y):
    visit[x][y] = 1
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(8):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<h and 0<=ny<w:
                if visit[nx][ny] == 0 and board[nx][ny] == 1:
                    visit[nx][ny] = 1
                    q.append([nx,ny])


while True:
    w,h = map(int,sys.stdin.readline().rstrip().split())

    if w == 0 and h ==0:
        break
    board = []
    for i in range(h):
        board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    visit = [[0]*w for _ in range(h)]
    
    answer = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and visit[i][j] == 0:
                answer += 1
                bfs(i,j)
    print(answer)
