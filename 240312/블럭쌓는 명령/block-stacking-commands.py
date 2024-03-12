n, k = map(int, input().split())
n_list = [0]*(n+1)

for _ in range(k):
    a, b = map(int, input().split())
    n_list[a] += 1
    if b + 1 <= n:
        n_list[b + 1] -= 1

prefix_sum = 0
for i in range(1, n + 1):
    prefix_sum += n_list[i]
    n_list[i] = prefix_sum

n_list.sort()
x = n // 2 + 1
print(n_list[x])