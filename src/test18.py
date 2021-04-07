from collections import deque
import sys

def bfs(x,y):
    dist[x][y] = 0
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(8):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<l and 0<=ny<l:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    l = int(sys.stdin.readline().rstrip())
    s_x,s_y = map(int,sys.stdin.readline().rstrip().split())
    e_x,e_y = map(int,sys.stdin.readline().rstrip().split())

    # board = [[0]*l for _ in range(l)]
    dist = [[-1]*l for _ in range(l)]

    bfs(s_x,s_y)
    print(dist[e_x][e_y])

