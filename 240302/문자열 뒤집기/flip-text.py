def equal(S):
    n = len(S)
    dp = [0] * n

    for i in range(1, n):
        if S[i] != S[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    if dp[-1] % 2 != 0:
        dp[-1] += 1

    return dp[-1] // 2

S = input()
print(equal(S))