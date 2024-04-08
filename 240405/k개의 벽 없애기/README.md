# 문제
https://www.codetree.ai/missions/2/problems/remove-k-walls?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 146ms <p>
Memory : 25MB

# 코드
```
from collections import deque
from itertools import combinations

n,k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sr,sc = map(int, input().split())
er,ec = map(int, input().split())

wall = [(i,j) for i in range(n) for j in range(n) if grid[i][j]]
wall_d = []
comb = combinations(wall,k)
dxs,dys = [0,1,0,-1], [1,0,-1,0]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x,y):
    if in_range(x,y) and not grid[x][y] and not visited[x][y] and step[x][y] == -1:
        return True
    if in_range(x,y) and grid[x][y] and visited[x][y] and step[x][y] == -1:
        return True
    return False

def bfs():
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy
            if can_go(nx,ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y]+1
                q.append((nx,ny))
                if nx==(er-1) and ny==(ec-1):
                    return step[nx][ny]
    return -1

for new_comb in comb:
    visited = [[False]*n  for _ in range(n)]
    step = [[-1]*n for _ in range(n)]
    q = deque()

    for c in new_comb:
        visited[c[0]][c[1]] = True
    q.append((sr-1,sc-1))
    visited[sr-1][sc-1] = True
    step[sr-1][sc-1] = 0
    wall_d.append(bfs())
wall_d.sort()
if wall_d[-1] !=-1:
    for w in wall_d:
        if w != -1:
            print(w)
            break
else:
    print(-1)
```
