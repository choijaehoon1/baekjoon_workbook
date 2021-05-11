import sys

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    n = int(sys.stdin.readline().rstrip())

    dp = []
    for i in range(2):
        dp.append(list(map(int,sys.stdin.readline().rstrip().split())))

    answer = 0
    if n == 1:
        answer = max(dp[0][0],dp[1][0])
    elif n >= 2:
        dp[0][1] += dp[1][0] # 초기(첫번째 칸은 정해져 있게 됨)
        dp[1][1] += dp[0][0] # 초기(첫번째 칸은 정해져 있게 됨)
        for i in range(2,n): # n 2일때는 자연스럽게 for문 안탐
            dp[1][i] += max(dp[0][i-1],dp[0][i-2]) # 왼쪽위와 왼쪽위에서 한칸전 비교(2가지 경우중 큰 것)
            dp[0][i] += max(dp[1][i-1],dp[1][i-2]) # 왼쪽아래와 왼쪽아래에서 한칸전 비교(2가지 경우중 큰 것)
        
        answer = max(dp[0][n-1],dp[1][n-1]) 
    print(answer)    

