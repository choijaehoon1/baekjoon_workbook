import sys
import heapq

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    visit = [0]*1000001
    k = int(sys.stdin.readline().rstrip())

    min_h = []
    max_h = []
    
    for i in range(k):
        oper,num = sys.stdin.readline().rstrip().split()
        if oper == 'I':
            i_num = int(num)
            heapq.heappush(min_h,[i_num,i])
            heapq.heappush(max_h,[-i_num,i])
            visit[i] = 1

        elif oper == 'D':
            if num == '-1':
                while min_h and visit[min_h[0][1]] == 0:
                    heapq.heappop(min_h)

                if min_h:
                    n,idx = heapq.heappop(min_h)
                    visit[idx] = 0

            elif num == '1':            
                while max_h and visit[max_h[0][1]] == 0:
                    heapq.heappop(max_h)
                if max_h:
                    n,idx = heapq.heappop(max_h)
                    visit[idx] = 0
    while min_h and visit[min_h[0][1]] == 0:
        heapq.heappop(min_h)

    while max_h and visit[max_h[0][1]] == 0:
        heapq.heappop(max_h)

    if min_h and max_h:
        a = -max_h[0][0]
        b = min_h[0][0]
        print(a,b)
    else:
        print("EMPTY")    

