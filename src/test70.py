import sys
from itertools import combinations
s = sys.stdin.readline().rstrip()
stack = []
s = list(s)
pair = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
        s[i] = ''
    if s[i] == ')':
        idx = stack.pop()            
        pair.append([idx,i])
        s[i] = ''
# print(s)        
# print(pair)     
   
result = set()
# 괄호를 제거하는 모든 경우의 수구하기
for i in range(len(pair)): # 0부터 len()-1까지 => 최소: 괄호 다 제거, 최대: 괄호 한개만 제거
    for combi in combinations(pair,i):
        S = s[:]
        for x,y in combi:
            S[x] = '('
            S[y] = ')'
        tmp = ''.join(S)
        if tmp not in result:
            result.add(tmp)

answer = sorted(result)
for i in answer:
    print(i)
    
