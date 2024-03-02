n = int(input())
num_list = [x for x in map(int, input().split())]
num_list.sort()
sum = sum(num_list)
count = n//3

for i in range(count):
    sum -= num_list[i]
print(sum)