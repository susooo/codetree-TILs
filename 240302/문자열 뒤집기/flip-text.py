s1 = list(input())
s2 = s1[::-1]
flag = True
count = 0

for i in range(len(s1)):
    if flag and s1[i] != s2[i]:
        flag = False
        count += 1
    elif not flag and s1[i] == s2[i]:
        flag = True
print(count)