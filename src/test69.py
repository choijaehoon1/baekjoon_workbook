import sys
s = sys.stdin.readline().rstrip()

flag = True
stack = []

for i in s:
    if i == '(' or i =='[':
        stack.append(i)
    else:
        if stack:
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
            if i == ']':
                if stack[-1] == '[':
                    stack.pop()                                    
        else:                    
            flag = False
            break
    
if stack:
    flag = False
answer = 0

if flag:
    stack = []
    s = s.replace('()','2')
    s = s.replace('[]','3')
    # print(s)

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i].isnumeric():
            num = int(s[i])            
            tmp = 1
            for j in range(len(stack)):
                if stack[j] == '(':
                    tmp *= 2
                elif stack[j] == '[':
                    tmp *= 3
            answer += (num * tmp)
        elif stack and stack[-1] == '(' and s[i] == ')':
            stack.pop()
        elif stack and stack[-1] == '[' and s[i] == ']':
            stack.pop()            
    print(answer)                
else:
    print(0)


