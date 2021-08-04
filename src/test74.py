import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

array = []

for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    array.append(tmp)

cnt = 0
for i in range(M):
    tmp = sys.stdin.readline().rstrip()
    if tmp in array:
        cnt += 1
print(cnt)        

