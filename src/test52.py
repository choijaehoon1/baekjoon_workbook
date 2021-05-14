from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())

def D_fun(a):
    flag = False
    a = (a*2) % 10000
    if a == B:
        flag = True        
    return flag,a        

def S_fun(a):
    flag = False
    if a == 0:
        a = 9999
    else:
        a -= 1        
    if a == B:
        flag = True        
    return flag,a        


def L_fun(a):
    new_a = (a%1000)*10 + a//1000
    flag = False
    if new_a == B:
        flag = True

    return flag,new_a

def R_fun(a):
    new_a = (a%10)*1000 + a//10 
    flag = False
    if new_a == B:
        flag = True

    return flag,new_a

for i in range(T):
    A,B = map(int,sys.stdin.readline().rstrip().split())    
    q = deque()
    q.append([A,''])
    cnt = 0
    flag = False
    visit = [0]*10000
    while q:
        a,tmp = q.popleft()
        if visit[a] == 0:
            flag, num = D_fun(a)
            d_tmp = tmp + 'D' 
            if flag:
                print(d_tmp)
                break
            else:
                visit[a] = 1
                q.append([num,d_tmp])

            flag, num = S_fun(a)
            s_tmp = tmp + 'S' 
            if flag:
                print(s_tmp)
                break
            else:
                visit[a] = 1
                q.append([num,s_tmp])

            flag, num = L_fun(a)
            l_tmp = tmp + 'L' 
            if flag:
                print(l_tmp)
                break
            else:
                visit[a] = 1
                q.append([num,l_tmp])

            flag, num = R_fun(a)
            r_tmp = tmp + 'R' 
            if flag:
                print(r_tmp)
                break
            else:
                visit[a] = 1
                q.append([num,r_tmp])

            cnt += 1            
    
