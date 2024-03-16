# 문제
[https://www.codetree.ai/missions/2/problems/number-of-happy-sequence/description](https://www.codetree.ai/missions/2/problems/number-of-happy-sequence?&utm_source=clipboard&utm_medium=text)

# 복잡도
Time : 163ms <p>
Memory : 25MB

# 코드
```
n,m = map(int, input().split())
grid = [list(map(int, input().split())) 
    for _ in range(n)]
result = 0

for i in range(n):
    num1,num2 = grid[i][0], grid[0][i]
    count1,count2 = 0,0
    for j in range(n):
        if grid[i][j] == num1:
            count1 += 1
            if count1 >= m:
                result += 1
                break
        else:
            num1 = grid[i][j]
            count1 = 1
    for k in range(n):
        if grid[k][i] == num2:
            count2 += 1
            if count2 >= m:
                result += 1
                break
        else:
            num2 = grid[k][i]
            count2 = 1
print(result)
```
