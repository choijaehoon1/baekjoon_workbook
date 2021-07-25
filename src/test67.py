import sys
from collections import deque
tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    N,M = map(int,sys.stdin.readline().rstrip().split())
    data =  list(map(int,sys.stdin.readline().rstrip().split()))

    q = deque()
    for i in range(N):
        q.append([data[i],i])
        
    tmp = []
    while q:
        priority,id = q.popleft()
        max_value = 0
        for i in q:
            max_value = max(max_value,i[0])
        if priority < max_value:
            q.append([priority,id])
        else:
            tmp.append([priority,id])
                
    answer = 0
    for i in range(len(tmp)):
        if tmp[i][1] == M:
            answer = i+1
            break
    print(answer)    
