import sys

def dfs(idx,length,tmp):
    if length == L:
        mo = 0
        vo = 0
        for i in tmp:
            if i in ['a','e','i','o','u']:
                mo += 1
            else:
                vo += 1
        if mo >= 1 and vo >=2:                    
            print(tmp)
        return
    for i in range(idx+1,C):
        dfs(i,length+1,tmp+alpha[i])

L,C = map(int,sys.stdin.readline().rstrip().split())
alpha = list(sys.stdin.readline().rstrip().split())
alpha.sort()

for i in alpha:
    idx = alpha.index(i)
    dfs(idx,1,i)
