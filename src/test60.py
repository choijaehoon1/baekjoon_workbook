import sys

N = int(sys.stdin.readline().rstrip())
stack = []
for i in range(N):
    # 주의: split 반환 = 리스트
    tmp_list = sys.stdin.readline().rstrip().split(' ')
    if len(tmp_list) == 2:
        stack.append(tmp_list[1])
    elif len(tmp_list) == 1:
        if tmp_list[0] == 'pop':
            if stack == []:
                print(-1)
            else:
                print(stack.pop())
        elif tmp_list[0] == 'size':
            print(len(stack))                
        elif tmp_list[0] == 'empty':
            if stack == []:
                print(1)           
            else:
                print(0)                
        elif tmp_list[0] == 'top':
            if stack == []:
                print(-1)           
            else:
                print(stack[-1])            
