from collections import Counter
import sys


def dfs(index,t):
    global answer
    if cnt + t == K:
        imsi = 0
        for arr in array:
            flag = False
            for a in arr:
                idx = ord(a) - ord('a')
                if alpha[idx] == 0:
                    flag = True
                    break
            if flag == False:
                imsi += 1 
        answer = max(answer,imsi)
        return

    for i in range(index, 26):
        if alpha[i] == 0:
            alpha[i] = 1
            dfs(i,t+1)
            alpha[i] = 0                    

N,K = map(int,sys.stdin.readline().rstrip().split())
alpha = [0 for _ in range(26)]
duple = "antatica"

cnt = 0
for i in duple:
    if alpha[ord(i) - ord('a')] == 0:
        alpha[ord(i) - ord('a')] += 1
        cnt += 1

array = []
tmp = []
for i in range(N):
    s = list(sys.stdin.readline().rstrip())
    n_str = s[4:-4]    
    array.append(n_str)

answer = 0
if K < cnt:
    print(0)
else:     
    dfs(0,0)
    print(answer)
