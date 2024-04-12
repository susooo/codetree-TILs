# 문제
https://www.codetree.ai/missions/2/problems/move-to-max-adjacent-cell-simultaneously?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 195ms <p>
Memory : 26MB

# 코드
```
from collections import deque
n,m,t = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
balls = [list(map(int,input().split())) for _ in range(m)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y,value):
    return in_range(x,y) and grid[x][y]>value

def simulate():
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    #구슬 이동하기
    while q:
        max_value = 0
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if can_go(nx,ny,max_value):
                max_x, max_y, max_value = nx,ny,grid[nx][ny]
        step[max_x][max_y] += 1

q = deque()
count = 0
for ball in balls:
    q.append((ball[0]-1,ball[1]-1))

while t:
    step = [[0]*n for _ in range(n)]
    simulate()
    for i in range(n):
        for j in range(n):
            if step[i][j] >= 2: #2개 이상인 구슬 제거
                step[i][j] = 0
            elif step[i][j] == 1: #1개인 구슬 q에 추가
                q.append((i,j))
    t-=1

#출력
for i in range(n):
    for j in range(n):
        if step[i][j] == 1:
            count += 1
print(count)
```
