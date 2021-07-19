import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
q = deque()

for i in range(1,N+1):
    q.append(i)
result = 0
while q:
    if len(q) == 1:
        result = q.popleft()
        break
    elif len(q) > 1:
        q.popleft()
        num = q.popleft()
        q.append(num)
print(result)        
