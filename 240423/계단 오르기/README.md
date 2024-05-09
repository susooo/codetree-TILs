# 문제
https://www.codetree.ai/missions/2/problems/climbing-stairs?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 151ms <p>
Memory : 24MB

# 코드
```
n = int(input())
dp = [0]*(n+1)

for i in range(2,n+1):
    if i==2:
        dp[2]=1
    elif i==3:
        dp[3] = 1
    else:
        dp[i] = dp[i-2] + dp[i-3]

print(dp[n]%10007)
```
