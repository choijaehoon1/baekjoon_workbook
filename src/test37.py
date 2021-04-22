from itertools import combinations
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
board = [[]]
chicken = []
home = []
for i in range(1,N+1):
    board.append([0]+list(map(int,sys.stdin.readline().rstrip().split())))
    for j in range(1,N+1):
        if board[i][j] == 2:
            chicken.append([i,j])
            board[i][j] = 0
        if board[i][j] == 1:     
            home.append([i,j])      

answer = int(1e9)
for combi in combinations(chicken,M):
    for cx,cy in combi:
        board[cx][cy] = 2

    total_dist = 0
    for hx,hy in home:
        dist = int(1e9)
        for cx,cy in combi:
            tmp = abs(hx-cx) + abs(hy-cy)
            dist = min(dist,tmp)
        total_dist += dist

    answer = min(answer,total_dist)

    for cx,cy in combi:
        board[cx][cy] = 0
print(answer)        
