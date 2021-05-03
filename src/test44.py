import sys

N = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))

result = [-1 for _ in range(N)]

stack = []
stack.append(0)
end = 1

while stack and end < N:
    while stack and data[stack[-1]] < data[end]:
        result[stack[-1]] = data[end]
        stack.pop()
    stack.append(end)        
    end += 1        
print(*result)
