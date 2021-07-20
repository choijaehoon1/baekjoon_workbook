# 시간초과 10만개를 in으로 확인하기 때문
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
q = deque()
data = deque()
result = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())    
    data.append(num)

tmp = 0
flag = True
while data:
    check = data.popleft()
    
    if check not in q:
        for i in range(tmp,check):
            q.append(i+1)
            result.append('+')
            tmp = check
        q.pop()            
        result.append('-')
    else:
        t = q.pop()
        if t == check:
            result.append('-')
        else:
            flag = False
            break            
        
if flag:
    for i in result:
        print(i)
else:
    print('NO')


