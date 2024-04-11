# 문제
https://www.codetree.ai/missions/2/problems/move-to-larger-adjacent-cell?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 139ms <p>
Memory : 25MB

# 코드
```
from collections import deque
n,r,c = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
answer = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs():
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if in_range(nx,ny) and grid[nx][ny]>grid[x][y]:
                q.append((nx,ny))
                answer.append(grid[nx][ny])
                break

q = deque()   
q.append((r-1,c-1))
answer.append(grid[r-1][c-1])
bfs()
print(*answer)
```
