import sys
from collections import Counter
import decimal

array = []

cnt = 0
while True:
    tmp = sys.stdin.readline().rstrip()
    if tmp == '':
        break
    array.append(tmp)
    cnt += 1
tmp_list = list(Counter(array).most_common())

data = []

num = 100/cnt

for i in tmp_list:
    s_num = str(i[1]*num)
    bi = round(decimal.Decimal(s_num),4)
    data.append([i[0],bi])
result = sorted(data, key=lambda x:x[1],reverse=True)    
answer = sorted(result, key=lambda x:x[0])    
# print(answer)

for i in answer:
    print(i[0],'%.4f' %i[1])


