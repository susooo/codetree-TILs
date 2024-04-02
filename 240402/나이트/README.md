# 문제
https://www.codetree.ai/missions/2/problems/knight-movements?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 161ms <p>
Memory : 25MB

# 코드
```
from collections import deque
n = int(input())
sr,sc,er,ec = map(int, input().split())
visited = [[False]*n for _ in range(n)]
dir8 =[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
d = [[0]*n for _ in range(n)]
q = deque()

def search(x,y,k):
    d[x][y] = k
    visited[x][y] = True
    q.append((x,y))

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx,ny = x+dir8[i][0], y+dir8[i][1]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny]:
                search(nx,ny,d[x][y]+1)

search(sr-1,sc-1,0)
bfs()
print(d[er-1][ec-1]) if visited[er-1][ec-1] else print(-1)
```
