import sys

N = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))

stack = []
stack.append(N-1)

left = N-2
result = [0] * len(data)
while stack and left >=0:
    while stack and data[left] >= data[stack[-1]]:
        result[stack[-1]] = left+1
        stack.pop()
    stack.append(left)
    left -= 1

print(*result)

