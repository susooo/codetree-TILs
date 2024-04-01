# 문제
https://www.codetree.ai/missions/2/problems/glacier?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 375ms <p>
Memory : 29MB

# 코드
```
from collections import deque

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
time = 0
water = deque()
glaciers = deque()

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

def is_water(x,y):
    return in_range(x,y) and not grid[x][y] and not visited[x][y]

def is_glacier(x,y):
    return in_range(x,y) and grid[x][y] and not visited[x][y]

def bfs():
    while water:
        x,y = water.popleft()
        for dx, dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy

            if is_water(nx, ny):
                water.append((nx,ny))
                visited[nx][ny] = True
            elif is_glacier(nx,ny):
                glaciers.append((nx,ny))
                visited[nx][ny] = True

def melt():
    while glaciers:
        x,y = glaciers.popleft()
        grid[x][y] = 0

def melting_simulation():
    global time, final_melted, water

    #step1. 첫 해안선 체크, 해안선 안 둘러싸인 빙하 체크
    bfs()
    #step2. 더 녹일 빙하가 있는지 체크
    if not glaciers:
        return False
    #step3. 빙하 녹이는 시간, 녹인 빙하 개수 업데이트
    time+=1
    final_melted=len(glaciers)
    #step4. 빙하를 녹여 해안선 범위 넓히기
    water = glaciers.copy()
    melt()
    return True

water.append((0,0))
visited[0][0] = True
while True:
    #step1. 빙하 녹여 해안선 확장
    glacier_exist = melting_simulation()
    #step2. 해안선 확장이 가능한지
    if not glacier_exist:
        break
print(time, final_melted)
```
