# 문제
https://www.codetree.ai/missions/2/problems/stay-out-of-rain?&utm_source=clipboard&utm_medium=text

# 복잡도
### solution1 <p>
Time : 546ms <p>
Memory : 31MB <p>

### solution2 <p>
Time : 240ms <p>
Memory : 28MB <p>

# 코드
```
#solution1
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



#solution2
from collections import deque
n,h,m = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
place = [(i,j) for i in range(n) for j in range(n) if grid[i][j]==3]

#bfs에 필요한 변수들
q = deque()
visited = [[False]*n for _ in range(n)]
step = [[0]*n for _ in range(n)]
dxs,dys = [0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x,y):
    return in_range(x,y) and grid[x][y] != 1 and not visited[x][y]

def search(nx,ny,new_step):
    q.append((nx,ny))
    visited[nx][ny] = True
    step[nx][ny] = new_step

def bfs():
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy

            if can_go(nx,ny):
                search(nx,ny,step[x][y]+1)

for x,y in place:
    search(x,y,0)
bfs()
for i in range(n):
    for j in range(n):
        if grid[i][j] != 2:
            print(0, end=' ')
        else:
            if not visited[i][j]:
                print(-1, end=' ')
            else:
                print(step[i][j], end=' ')
    print()
```
