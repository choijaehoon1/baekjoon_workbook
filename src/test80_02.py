import sys
import heapq
N = int(sys.stdin.readline().rstrip())
max_h = []
min_h = []

visit = [0]*100001
for i in range(N):
    P,L = map(int,sys.stdin.readline().rstrip().split())
    heapq.heappush(max_h,[-L,-P])
    heapq.heappush(min_h,[L,P])
    visit[P] = 1
    
M = int(sys.stdin.readline().rstrip())
for i in range(M):
    oper = list(sys.stdin.readline().rstrip().split())
    if oper[0] == 'add':
        heapq.heappush(max_h,[-int(oper[2]),-int(oper[1])])
        heapq.heappush(min_h,[int(oper[2]),int(oper[1])])
        visit[int(oper[1])] = 1

    if oper[0] == 'solved':
        visit[int(oper[1])] = 0
        
    if oper[0] == 'recommend':
        if oper[1] == '1':
            while max_h and visit[-max_h[0][1]] == 0:
                heapq.heappop(max_h)
            if max_h:
                print(-max_h[0][1])

        if oper[1] == '-1':                    
            while min_h and visit[min_h[0][1]] == 0:
                a,b = heapq.heappop(min_h)
            if min_h:
                print(min_h[0][1])    
