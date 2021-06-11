import sys

stack = []
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    tmp = sys.stdin.readline().rstrip().split(' ')
    if tmp[0] == 'push':
        stack.append(tmp[1])
    elif tmp[0] == 'pop':
        if stack == []:
            print(-1)
        else:                
            num = stack.pop()
            print(num)
    elif tmp[0] == 'size':
        print(len(stack))
    elif tmp[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)            
    elif tmp[0] == 'top':
        if stack == []:
            print(-1)
        else:
            num = stack[-1]      
            print(num)

