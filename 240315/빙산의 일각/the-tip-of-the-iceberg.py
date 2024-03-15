n = int(input())
num = []
count = 0
for i in range(n):
    h = int(input())
    num.append(h)
mid_h = max(num)//2
min_h, max_h = min(num), max(num)

while min_h != mid_h:
    tmp = 0
    for j in range(n-1):
        if num[j]-mid_h > 0 and num[j+1]-mid_h <= 0:
            tmp += 1
    if num[n-1]-mid_h > 0:
        tmp += 1
    if tmp > count:
        count = tmp
        mid_h = (min_h+mid_h)//2
print(count)