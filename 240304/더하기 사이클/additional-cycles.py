num = int(input())
num2 = num
answer = 0
result = 0
flag = True

while flag:
    if len(str(num)) == 2:
        result = num//10
        result += num%10
    elif len(str(num)) == 1:
        result = num
    num = (num%10)*10 + result%10
    answer += 1
    if num == num2:
        print(answer)
        break