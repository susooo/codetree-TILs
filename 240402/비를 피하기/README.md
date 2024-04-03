# 문제
https://www.codetree.ai/missions/2/problems/stay-out-of-rain?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 546ms <p>
Memory : 31MB

# 코드
```
from collections import deque
n,h,m = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
final_d = [[0]*n for _ in range(n)]
people = deque()

dx,dy = [0,1,0,-1],[1,0,-1,0]
def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n or grid[nx][ny]==1:
                continue
            if grid[nx][ny]!=3 and not visited[nx][ny]:
                visited[nx][ny] = True
                d[nx][ny] = d[x][y]+1
                q.append((nx,ny))
            elif grid[nx][ny]==3 and not visited[nx][ny]:
                return d[x][y]+1
    return -1

for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            people.append((i,j))

while people:
    visited = [[False]*n for _ in range(n)]
    d = [[0]*n for _ in range(n)]
    q = deque()

    px,py = people.popleft()
    visited[px][py] = True
    q.append((px,py))
    final_d[px][py] = bfs()

for i in range(n):
    for j in range(n):
        print(final_d[i][j],end=' ')
    print('')
```
