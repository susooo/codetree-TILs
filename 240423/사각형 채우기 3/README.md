# 문제
https://www.codetree.ai/missions/2/problems/rectangle-fill-3?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 121ms <p>
Memory : 24MB

# 코드
```
n = int(input())
if n<3:
    dp = [0]*(3)
else:
    dp = [0]*(n+1)

dp[0],dp[1],dp[2] = 1,2,7
for i in range(3,n+1):
    dp[i] = (3*dp[i-1] + dp[i-2] - dp[i-3])%1000000007

print(dp[n])
```
