import sys
from collections import deque
message = sys.stdin.readline().rstrip()
message = message.replace('()','0')

stack = []
answer = 0

for i in message:
    if i == '0':
        answer += len(stack)
    else:
        if i == '(':
            stack.append('(')
        elif i == ')' and stack:
            stack.pop()
            answer += 1            
print(answer)
