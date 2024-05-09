# 문제
https://www.codetree.ai/missions/2/problems/maximin-path-in-square?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 163ms <p>
Memory : 25MB

# 코드
```
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = grid[0][0]
for i in range(1, n):
    dp[0][i] = grid[0][i] if dp[0][i-1] > grid[0][i] else dp[0][i-1]

    dp[i][0] = grid[i][0] if dp[i-1][0] > grid[i][0] else dp[i-1][0]

for x in range(1, n):
    for y in range(1, n):
        dp[x][y] = min(max(dp[x-1][y], dp[x][y-1]), grid[x][y])

print(dp[n-1][n-1])
```
