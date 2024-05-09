# 문제
https://www.codetree.ai/missions/2/problems/longest-increasing-subsequence?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 138ms <p>
Memory : 25MB

# 코드
```
n = int(input())
n_list = list(map(int,input().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if n_list[j] < n_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
```
