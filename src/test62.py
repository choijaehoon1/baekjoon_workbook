import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
q = deque()
for i in range(N):
    # 주의: split 반환 = 리스트
    tmp_list = sys.stdin.readline().rstrip().split(' ')
    if len(tmp_list) == 2:
        q.append(tmp_list[1])
    elif len(tmp_list) == 1:
        if tmp_list[0] == 'pop':
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif tmp_list[0] == 'size':
            print(len(q))                
        elif tmp_list[0] == 'empty':
            if len(q) == 0:
                print(1)           
            else:
                print(0)                
        elif tmp_list[0] == 'front':
            if len(q) == 0:
                print(-1)           
            else:
                print(q[0])            
        elif tmp_list[0] == 'back':
            if len(q) == 0:
                print(-1)           
            else:
                print(q[-1])                            
