from collections import deque
import sys

def bfs(start):
    visit[start] = 1
    binary[start] = 1
    q = deque()
    q.append(start)
    while q:
        n = q.popleft()
        for i in board[n]:
            if binary[i] == 0:
                binary[i] = -binary[n]
                visit[i] = 1
                q.append(i)
            else:
                if binary[i] == binary[n]:
                    return True
    return False

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    V,E = map(int, sys.stdin.readline().rstrip().split())

    board = [[] for _ in range(V+1)]
    visit = [0 for _ in range(V+1)]
    binary = [0 for _ in range(V+1)]

    for i in range(E):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        board[a].append(b)
        board[b].append(a)

    flag = False
    for i in range(1,V+1):
        if binary[i] == 0 and visit[i] == 0:
            flag = bfs(i)
            if flag == True:
                break

    if flag:
        print("NO")
    else:
        print("YES")    

