import sys
from collections import deque
N,K = map(int,sys.stdin.readline().rstrip().split())

q = deque()
for i in range(1,N+1):
    q.append(i)

result = []

cnt = 0
while q:
    num = q.popleft()
    cnt += 1
    if cnt >= K:
        result.append(num)
        cnt = 0
    else:
        q.append(num)

print('<' + ', '.join(map(str,result)) + '>')
