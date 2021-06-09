from collections import deque
from itertools import combinations
import sys

def bfs(group):
    if len(group) == 1:
        value = 0
        for i in group:
            value = person[i]
        return 1, value

    elif len(group) >= 2:
        tmp = [0]*N
        q = deque()
        q.append(group[0])
        tmp[group[0]] = 1
        cnt = 1
        value = 0
        
        while q:
            x = q.popleft()
            value += person[x]
            for i in range(N):
                if board[x][i] == 1 and i in group and tmp[i] == 0:
                    tmp[i] = 1
                    cnt += 1
                    q.append(i)
            
        return cnt,value                                
    
N = int(sys.stdin.readline().rstrip())
person = list(map(int,sys.stdin.readline().rstrip().split()))

board = [[0]*(N) for _ in range(N)]
for i in range(N):
    data = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in data[1:]:
        board[i][j-1] = 1
        board[j-1][i] = 1

answer = int(1e9)
for i in range(1,N//2+1):
    for combi in combinations(range(N),i):
        grp01 = list(combi)
        grp02 = []
        for j in range(N):
            if j not in grp01:
                grp02.append(j)
        cnt01,value01 = bfs(grp01)
        cnt02,value02 = bfs(grp02)
        # print(grp01,grp02)
        # print(cnt01,cnt02)
        if cnt01 + cnt02 == N:
            answer = min(answer,abs(value01-value02))

if answer == int(1e9):
    print(-1)
else:    
    print(answer)        
