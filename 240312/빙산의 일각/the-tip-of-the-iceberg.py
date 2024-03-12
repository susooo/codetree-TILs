n = int(input())
num = []
count = 0
for i in range(n):
    h = int(input())
    num.append(h)
set_num = set(num)

for i in set_num:
    tmp = 0
    for j in range(n-1):
        if num[j]-i > 0 and num[j+1]-i <= 0:
            tmp += 1
    if num[n-1]-i > 0:
        tmp += 1
    if tmp > count:
        count = tmp
print(count)