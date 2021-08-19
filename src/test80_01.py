# 시간초과
import sys
N = int(sys.stdin.readline().rstrip())

dic = dict()
for i in range(N):
    P,L = map(int,sys.stdin.readline().rstrip().split())
    dic[P] = L
    
# print(dic)    
M = int(sys.stdin.readline().rstrip())
for i in range(M):
    oper = list(sys.stdin.readline().rstrip().split())
    if oper[0] == 'add':
        dic[int(oper[1])] = int(oper[2])
    if oper[0] == 'solved':
        del dic[int(oper[1])]        
    if oper[0] == 'recommend':
        if oper[1] == '1':
            # print(dic.items()) # 딕셔너리가 리스트 형태로 됨(리스트안에 튜플 형태)
            tmp = sorted(dic.items(),key=lambda x:(-x[1],-x[0]))
            print(tmp[0][0])
        elif oper[1] == '-1':                    
            tmp = sorted(dic.items(),key=lambda x:(x[1],x[0]))
            print(tmp[0][0])

