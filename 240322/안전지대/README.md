# 문제
[https://www.codetree.ai/missions/2/problems/best-place-of-33?&utm_source=clipboard&utm_medium=text](https://www.codetree.ai/missions/2/problems/comfort-zone?&utm_source=clipboard&utm_medium=text)

# 복잡도
Time : 1514ms <p>
Memory : 145MB

# 코드
```
import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(n)]
min_k, max_k = 1, max(map(max, village))
final_k, safe_zone = 1,0

def dfs(k,x,y):
    global count
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if village[nx][ny]>k and not visited[nx][ny]:
            visited[nx][ny]=True
            count += 1
            dfs(k,nx,ny)
    return count

while min_k != max_k:
    visited = [[False]*m for _ in range(n)]
    k_count = []
    for i in range(n):
        for j in range(m):
            count = 0
            if village[i][j]>min_k and not visited[i][j]:
                visited[i][j]=True
                count += 1
                k_count.append(dfs(min_k,i,j))
            if safe_zone < len(k_count):
                safe_zone = len(k_count)
                final_k = min_k
    min_k+=1
print(final_k, safe_zone)
```
