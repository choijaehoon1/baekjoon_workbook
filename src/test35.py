     
N = int(input())
T = int(input())

table = list(map(int, input().split()))
vote = [0 for _ in range(T+1)]
dp = []
for i in range(len(table)):
    flag = False
    for d in dp:
        if table[i] == d[2]:
            d[0] += 1
            flag = True
            break
    if flag == True:
        continue
    if len(dp) < N:
        vote[table[i]] += 1
        dp.append([vote[table[i]],i,table[i]])
    else:
        dp.sort(key = lambda x:(x[0],x[1]))
        cnt,date,num = dp.pop(0)
        vote[num] = 0
        vote[table[i]] += 1
        dp.append([vote[table[i]],i,table[i]])

answer = []
for i in dp:
    answer.append(i[2])
answer.sort()
print(*answer)    


