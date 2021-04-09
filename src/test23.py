from collections import deque
import sys

def move(x,y,dx,dy):
    cnt = 0
    # 주어진 조건에서 모든 끝은 막혀있으니 바깥으로 나가는 경우는 없음
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x,y,cnt        

def bfs(r_x,r_y,b_x,b_y,time):
    q = deque()
    q.append([r_x,r_y,b_x,b_y,time])
    visit[r_x][r_y][b_x][b_y] = 1

    while q:
        r_x,r_y,b_x,b_y,time = q.popleft()
        if time > 10: # 리턴이 아님
            break
        for k in range(4):
            rnx, rny, rcnt = move(r_x,r_y,dx[k],dy[k])
            bnx, bny, bcnt = move(b_x,b_y,dx[k],dy[k])
            
            if board[bnx][bny] != 'O':
                if board[rnx][rny] == 'O':
                    print(time)
                    return # 끝냄

                if rnx == bnx and rny == bny:
                    if rcnt > bcnt:
                        rnx -= dx[k]
                        rny -= dy[k]                    
                    else:    
                        bnx -= dx[k]
                        bny -= dy[k]                   

                if visit[rnx][rny][bnx][bny] == 0:
                    visit[rnx][rny][bnx][bny] = 1
                    q.append([rnx,rny,bnx,bny,time+1])
    # 실패하는 경우는 많음(시간 경과하거나 파란색만 빠지는 경우이거나 빨간색 파란색 같이빠지는 경우)                    
    print(-1) # 따라서 함수반환 값을 실패하는 경우인 -1로 설정

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int, sys.stdin.readline().rstrip().split())
board = []

for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))
    for j in range(M):
        if board[i][j] == 'R':
            r_x,r_y = i,j
        elif board[i][j] == 'B':
            b_x,b_y = i,j
visit = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
bfs(r_x,r_y,b_x,b_y,1)

