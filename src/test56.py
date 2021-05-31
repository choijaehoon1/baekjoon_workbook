import sys
sys.setrecursionlimit(10**6)

def dfs(start,tmp):
    visit[start] = 1
    
    for i in board[start]:
        if visit[i] == 0:
            dfs(i,tmp)
        if i == tmp:
            answer.append(tmp)
            return


N = int(sys.stdin.readline().rstrip())
first = [i for i in range(N+1)]
second = [0]
board = [[] for _ in range(N+1)]
for i in range(1,N+1):
    board[i].append(int(sys.stdin.readline().rstrip()))

answer = []
for i in range(1,N+1):
    visit = [0 for _ in range(N+1)]
    dfs(first[i],first[i])
# print(answer)
print(len(answer))
answer.sort()
for i in answer:
    print(i)

