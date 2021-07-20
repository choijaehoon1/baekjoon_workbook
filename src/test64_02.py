# 스택 활용
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
q = deque()
data = deque()
result = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())    
    data.append(num)

tmp = 1
flag = True
while data:
    check = data.popleft()
    
    while tmp <= check:
        result.append('+')
        q.append(tmp)
        tmp += 1

    if q[-1] == check:
        q.pop()
        result.append('-')
    else:
        flag = False        
        break
        
if flag:
    for i in result:
        print(i)
else:
    print('NO')


