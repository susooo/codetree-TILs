# 문제
https://www.codetree.ai/missions/2/problems/escape-with-min-distance?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 141ms <p>
Memory : 26MB

# 코드
```
from collections import deque
n,m = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
distance = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
q = deque()

def search(x,y,d):
    distance[x][y] = d
    visited[x][y] = True
    q.append((x,y))

def bfs():
    dx,dy = [0,1,0,-1], [1,0,-1,0]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if grid[nx][ny] and not visited[nx][ny]:
                search(nx,ny,distance[x][y]+1)
            
            

search(0,0,0)
bfs()
print(distance[n-1][m-1]) if visited[n-1][m-1] else print(-1)
```
