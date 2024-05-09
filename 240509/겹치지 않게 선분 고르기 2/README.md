# 문제
https://www.codetree.ai/missions/2/problems/select-segments-without-overlap-2?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 175ms <p>
Memory : 25MB

# 코드
```
n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda x: (x[1], -x[0]))

dp = [0] * n
dp[0] = 1
for i in range(1, n):
    dp[i] = dp[i-1]

    for j in range(i-1, -1, -1):
        if lines[j][1] < lines[i][0]:
            dp[i] = max(dp[i], dp[j] + 1)
            break

print(max(dp))
```
