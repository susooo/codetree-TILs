# 문제
https://www.codetree.ai/missions/2/problems/longest-increasing-sequence-2d?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 158ms <p>
Memory : 25MB

# 코드
```
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        dp[i][j] = -1

dp[0][0] = 1
for i in range(n):
    for j in range(m):
        for k in range(i):
            for l in range(j):
                if dp[k][l] == -1:
                    continue
                if grid[k][l] < grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[k][l]+1)
                
answer = -1
for i in range(n):
    for j in range(m):
        answer = max(answer, dp[i][j])
print(answer)
```
