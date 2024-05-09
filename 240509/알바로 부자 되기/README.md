# 문제
https://www.codetree.ai/missions/2/problems/being-rich-by-working-part-time?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 281ms <p>
Memory : 25MB

# 코드
```
n = int(input())
info = [list(map(int,input().split())) for _ in range(n)]
info.sort(key=lambda x: (x[1], -x[0]))

dp = [0] * n
dp[0] = info[0][2]

for i in range(1, n):
    dp[i] = max(dp[i-1], info[i][2])

    for j in range(i-1, -1, -1):
        if info[j][1] < info[i][0]:
            dp[i] = max(dp[i], dp[j] + info[i][2])
            break

print(max(dp))
```
