import sys
input = sys.stdin.readline
n, k = map(int, input().split())
n_list = [0]*(n+1)
for i in range(k):
    a,b = map(int, input().split())
    for j in range(a, b+1):
        n_list[j] += 1
n_list.sort()
x = n//2+1
print(n_list[x])