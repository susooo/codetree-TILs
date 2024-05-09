# 문제
https://www.codetree.ai/missions/2/problems/minimum-sum-path-in-square?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 126ms <p>
Memory : 25MB

# 코드
```
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][n-1] = grid[0][n-1]
for i in range(n-2,-1,-1):
    dp[0][i] = dp[0][i+1] + grid[0][i]

for i in range(1,n):
    dp[i][n-1] = dp[i-1][-1] + grid[i][n-1]

for i in range(1,n):
    for j in range(n-2,-1,-1):
        dp[i][j] = min(dp[i][j+1], dp[i-1][j]) + grid[i][j]

print(dp[n-1][0])
```
