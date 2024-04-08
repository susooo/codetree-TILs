# 문제
https://www.codetree.ai/missions/2/problems/oranges-have-gone-bad?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 238ms <p>
Memory : 28MB

# 코드
```
from collections import deque
n,k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

dxs,dys = [0,1,0,-1],[1,0,-1,0]
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x,y):
    return in_range(x,y) and grid[x][y] and step[x][y]==-1

def bfs():
    while q:
        x,y,c = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if can_go(nx,ny):
                step[nx][ny] = c+1 
                q.append((nx,ny,c+1))

q = deque()
step = [[-1]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            q.append((i,j,0))
            step[i][j] = 0

bfs()
for i in range(n):
    for j in range(n):
        if grid[i][j] and step[i][j]==-1:
            print(-2, end=' ')
        else:
            print(step[i][j], end=' ')
    print()
```
