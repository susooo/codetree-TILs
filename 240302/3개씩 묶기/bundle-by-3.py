n = int(input())
num_list = [x for x in map(int, input().split())]
num_list.sort(reverse=True)
sum = sum(num_list)

for i in range(0,len(num_list),3):
    if i+2 <= len(num_list):
        sum -= num_list[i+2]
    if i+3 > len(num_list):
        break
print(sum)