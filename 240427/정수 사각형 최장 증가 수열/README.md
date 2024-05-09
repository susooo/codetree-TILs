# 문제
https://www.codetree.ai/missions/2/problems/lis-on-the-integer-grid?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 857ms <p>
Memory : 58MB

# 코드
```
from collections import deque
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[1]*n for _ in range(n)]

order = []
for i in range(n):
    for j in range(n):
        order.append((grid[i][j], i, j))

order.sort()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for _, x, y in order:
    dxs, dys = [0,1,0,-1], [1,0,-1,0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dp[i][j])
print(answer)
```
