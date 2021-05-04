import sys
N = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))

result = [0 for _ in range(N)]
stack = []

stack.append(N-1)
end = N-2
while stack and end >=0:
    while stack and data[end] >= data[stack[-1]]:
        result[stack[-1]] = end+1
        stack.pop()
    stack.append(end)
    end -= 1        
print(*result)

