import sys

N = int(sys.stdin.readline().rstrip())
tmp = []
for i in range(N):
    tmp.append(list(sys.stdin.readline().rstrip()))

alpha = [0 for _ in range(26)]

for i in tmp:
    length = len(i)
    for j in range(len(i)):
        idx = ord(i[j]) - ord('A')
        alpha[idx] += 10**(length-j-1)

alpha.sort(reverse=True)

result = 0        
num = 9
for i in alpha:
    if i != 0:
        result += (i*num)
        num -= 1
print(result)        

