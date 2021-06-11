import sys

stack = []
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    tmp = list(sys.stdin.readline().rstrip())
    if tmp[0] == 'p' and tmp[1] == 'u':
        idx = tmp.index(' ')
        num = ''.join(tmp[idx+1:])
        stack.append(num)
    elif tmp[0] == 'p' and tmp[1] == 'o':
        if stack == []:
            print(-1)
        else:                
            num = stack.pop()
            print(num)
    elif tmp[0] == 's':
        print(len(stack))
    elif tmp[0] == 'e':
        if stack == []:
            print(1)
        else:
            print(0)            
    elif tmp[0] == 't':
        if stack == []:
            print(-1)
        else:
            num = stack[-1]      
            print(num)

