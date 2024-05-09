# 문제
https://www.codetree.ai/missions/2/problems/increasing-and-descreasing-subsequence?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 156ms <p>
Memory : 25MB

# 코드
```
n = int(input())
nums = list(map(int,input().split()))

def increase(nums):
    up = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                up[i] = max(up[i], up[j] + 1)
    return up

def decrease(nums):
    down = [1] * n
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                down[i] = max(down[i], down[j] + 1)
    return down

def length(nums):
    up = increase(nums)
    down = decrease(nums)

    max_len = 0
    for i in range(n):
        max_len = max(max_len, up[i] + down[i] - 1)
    return max_len

print(length(nums))
```
