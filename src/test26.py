import sys

def dfs(node):
    global answer
    visit[node] = 1
    loop.append(node) # loop에 추가
    num = table[node] # 원하는 학생 저장

    if visit[num] == 1: # 사이클이면 즉 다시 돌아오게 되ㅣ면
        if num in loop: # 원하는 학생이 지나왔던 루프에 있는 경우에만 리스트 슬라이싱해서 더함
            answer += loop[loop.index(num):] # 리스트 슬라이싱하면 리스트가 반환되므로 더하기 연산 가능
        return
    else: # 방문하지 않았으면 해당 숫자로 재귀 수행
        dfs(num)        

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    answer = []
    n = int(sys.stdin.readline().rstrip())
    table = [0] + list(map(int,sys.stdin.readline().rstrip().split()))
    visit = [1] + [0]*n # 방문했던거 또 방문할 필요 없음(백트래킹이 아니므로)
    for i in range(1,n+1):
        if visit[i] == 0:
            loop = [] # 방문했던 노드들 담겨 있는 리스트
            dfs(i)
    print(n-len(answer))

