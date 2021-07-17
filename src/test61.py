import sys

tc = int(sys.stdin.readline().rstrip())

for _ in range(tc):
    stack = []
    data = list(sys.stdin.readline().rstrip())
    flag = True
    for i in data:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack == []:
                flag = False            
                break
            elif stack[-1] == ')':
                flag = False            
                break
            elif stack[-1] == '(':
                stack.pop()
    
    if stack != []:
        flag = False

    if flag:
        print('YES')
    else:
        print('NO')                        

