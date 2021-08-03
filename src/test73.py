import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

dic = dict()
reverse_dic = dict()
for i in range(1,N+1):
    tmp = sys.stdin.readline().rstrip()
    dic[i] = tmp
    reverse_dic[tmp] = i

for i in range(M):
    test = sys.stdin.readline().rstrip()
    if test.isnumeric():
        idx = int(test)
        print(dic[idx])        
    else:
        print(reverse_dic[test])        

