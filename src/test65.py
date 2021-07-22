import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
data = sys.stdin.readline().rstrip()
tmp = deque()
dic = {}
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    tmp.append(num)

for i in data:    
    if i.isalpha() and i not in dic:
        dic[i] = tmp.popleft()
# print(dic)        
        
stack = []
for d in data:
    if d.isalpha():
        stack.append(dic[d])
    else:
        if d == '+' and len(stack) >=2:
            a=stack.pop()
            b=stack.pop()
            stack.append(b+a)
        elif d == '-' and len(stack) >=2:
            a=stack.pop()
            b=stack.pop()
            stack.append(b-a)
        elif d == '*' and len(stack) >=2:
            a=stack.pop()
            b=stack.pop()
            stack.append(b*a)
        elif d == '/' and len(stack) >=2:
            a=stack.pop()
            b=stack.pop()
            stack.append(b/a)

print(format(stack[0],'0.2f'))
