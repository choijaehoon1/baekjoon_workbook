from collections import deque
import sys

def find():
    result = []
    for i in range(N):
        for j in range(N):
            if 1 <= board[i][j] < size:
                result.append([i,j])

    return result

def check(result):
    tmp = []
    dist = [[-1]*N for _ in range(N)]
    dist[s_x][s_y] = 0
    q = deque()
    q.append([s_x,s_y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N and dist[nx][ny] == -1 and board[nx][ny] <= size:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])

    for r_x,r_y in result:
        if dist[r_x][r_y] != -1:
            tmp.append([dist[r_x][r_y],r_x,r_y])    
    if tmp != []:
        tmp.sort(key=lambda x:(x[0],x[1],x[2]))  
        return tmp[0]
    return None        

N = int(sys.stdin.readline().rstrip())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(N):
        if board[i][j] == 9:
            s_x,s_y = i,j
            board[i][j] = 0

size = 2
dx = [-1,1,0,0]
dy = [0,0,-1,1]

time = 0
ate = 0
while True:
    result = find()
    if result == []:
        break
    tmp = check(result)   
    if tmp == None:
        break
    dist,x,y = tmp[0],tmp[1],tmp[2]
    time += dist
    board[x][y] = 0
    s_x,s_y = x,y
    ate += 1

    if ate >= size:
        ate = 0 
        size += 1
print(time)
