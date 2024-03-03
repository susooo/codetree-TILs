n_list = [x for x in map(int, input().split())]
n_list.sort()
answer = 1
for num in n_list:
    if num%2 != 0:
        answer*=num
if answer == 1:
    answer = n_list[0]*n_list[1]*n_list[2]
print(answer)