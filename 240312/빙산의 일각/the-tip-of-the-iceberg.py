n = int(input())
num = []
count = 0
for i in range(n):
    h = int(input())
    num.append(h)
max_h = max(num)
min_h = min(num)
for i in range(min_h,max_h):
    tmp = 0
    for j in range(n):
        if num[j]-i == 0:
            tmp += 1
    if num[n-1] != 0:
        tmp += 1
    if tmp > count:
        count = tmp
print(count)