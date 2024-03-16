# 문제
https://www.codetree.ai/missions/2/problems/graph-traversal?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 227ms <p>
Memory : 26MB

# 코드
```
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    global result
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            result += 1
            dfs(i)

visited[1] = True
dfs(1)
print(result)
```
