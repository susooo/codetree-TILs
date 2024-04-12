# 문제
https://www.codetree.ai/missions/2/problems/escape-maze-with-wall-following?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 170ms <p>
Memory : 26MB

# 코드
```
from collections import deque
n = int(input())
x,y = map(int,input().split())
grid = [[None]*n for _ in range(n)]
for i in range(n):
    row = input().strip()
    for j in range(n):
        grid[i][j] = row[j]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def wall_exist(x,y):
    return in_range(x,y) and grid[x][y]=='#'

def bfs():
    index = 0
    time = 0
    dxs,dys = [0,1,0,-1],[1,0,-1,0]
    while q:
        x,y = q.popleft()
        nx,ny = x+dxs[index], y+dys[index]
        
        if visited[x][y][index]:
            return -1

        visited[x][y][index] = True
        if wall_exist(nx,ny): #시계 반대방향 이동
            index = (index-1+4)%4
            q.append((x,y))
        elif not in_range(nx,ny): #밖으로 이동
            time+=1
            return time
        else: 
            rx,ry = nx+dxs[(index+1)%4], ny+dys[(index+1)%4]
            if wall_exist(rx,ry): #한칸 이동
                q.append((nx,ny))
                time+=1
            else: #시계 방향 이동
                nx,ny = rx,ry
                index = (index+1+4)%4
                q.append((nx,ny))
                time+=2
    return time

q = deque()
q.append((x-1,y-1))
visited = [[[False for _ in range(4)] for _ in range(n)] for _ in range(n)]
final_time = bfs()
print(final_time) if final_time else print(-1)
```
