# 문제
https://www.codetree.ai/missions/2/problems/minimax-path-in-square?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 149ms <p>
Memory : 25MB

# 코드
```
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

# 0행, 0열 초기화
for i in range(n):
    dp[i][0] = max(dp[i-1][0], grid[i][0])
    dp[0][i] = max(dp[0][i-1], grid[0][i])

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[n-1][n-1])
```
