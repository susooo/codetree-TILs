# 문제
https://www.codetree.ai/missions/2/problems/fibonacci-number?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 142ms <p>
Memory : 24MB

# 코드
```
n = int(input())
dp = [-1]*(n+1)

def fib(n):
    if dp[n] != -1:
        return dp[n]
    if n <= 2:
        dp[n] = 1
    else:
        dp[n] = fib(n-2)+fib(n-1)
    return dp[n]

print(fib(n))
```
