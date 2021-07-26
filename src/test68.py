import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))

answer = []
q = deque()

for i in range(1,N+1):
    q.append([data[i-1],i])

cnt, num = q.popleft()
answer.append(num)
tmp = 0
while q:
    tmp += 1
    if cnt > 0:
        c,n = q.popleft()
        if tmp >= cnt:
            cnt = c
            tmp = 0
            answer.append(n)
        else:
            q.append([c,n])
    elif cnt < 0: 
        if tmp > abs(cnt):
            c,n = q.popleft()
            cnt = c
            tmp = 0
            answer.append(n)
        else:
            c,n = q.pop()
            q.appendleft([c,n])
print(*answer)


