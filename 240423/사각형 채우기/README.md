# 문제
https://www.codetree.ai/missions/2/problems/rectangle-fill?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 121ms <p>
Memory : 24MB

# 코드
```
n = int(input())
dp = [0]*(n+1)

for i in range(1,n+1):
    if i<=3:
        dp[i] = i
    else:
        dp[i]=(dp[i-2]+dp[i-1])%10007
print(dp[n])
```
