# 문제
https://www.codetree.ai/missions/2/problems/maximum-number-of-jumps?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 142ms <p>
Memory : 25MB

# 코드
```
n = int(input())
n_list = list(map(int, input().split()))
dp = [-1] * n

dp[0] = 0
for i in range(1, n):
    for j in range(i):
        if dp[j] == -1:
            continue
        if j + n_list[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
```
