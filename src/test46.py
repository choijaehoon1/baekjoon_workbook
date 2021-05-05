import heapq
from collections import deque
import sys

N,k = map(int,sys.stdin.readline().rstrip().split())
customer = deque()
for i in range(N):
    customer.append(list(map(int,sys.stdin.readline().rstrip().split())))

h = [] # 우선순위 큐
possible_counter = [] # 가능한 카운터
cnt = 0
time = 0
r = 1
answer = 0
while customer:
    while cnt < k and customer: # 앞에 줄선사람부터 카운터에 가까운 순서대로 배치
        id,w = customer.popleft()
        heapq.heappush(h,[time+w,-(cnt+1),id]) # 시간, -카운터번호: 내림차순(맥스 힙), 아이디
        cnt += 1

    if cnt >= k: # 카운터가 꽉찬 경우
        finish_time,c,id = heapq.heappop(h)  
        time = finish_time # 가장 시간이 적게 걸리는 시간으로 갱신
        heapq.heappush(possible_counter,-c) # 해당 카운터는 빠지므로 가능한 카운터에 번호 추가
        answer += r*id
        r += 1

        # 같이 끝나는 카운터 있으면 빼주기
        while customer and h and h[0][0] == time: 
            finish_time,c,id = heapq.heappop(h)
            answer += r*id
            r += 1
            heapq.heappush(possible_counter,-c)

        # 가능한 카운터가 있으면 고객 배치
        while customer and possible_counter:
            id,w = customer.popleft()            
            finish_time = time + w
            c = heapq.heappop(possible_counter)
            heapq.heappush(h,[finish_time,-c,id])

# 우선순위큐에 남아 있는 값 처리
while h:
    finish_time,c,id = heapq.heappop(h)
    answer += r*id
    r += 1
print(answer)            
