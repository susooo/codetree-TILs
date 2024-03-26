# 문제
https://www.codetree.ai/missions/2/problems/clear-stones-well?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 272ms <p>
Memory : 27MB

# 코드
```
from collections import deque
from itertools import combinations

n,k,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starts = []
for _ in range(k):
    r,c = map(int, input().split())
    starts.append((r-1,c-1))

q = deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]
max_count = 0

stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            stones.append((i,j))
stones = list(combinations(stones,m))

while stones:
    visited = [[False]*n for _ in range(n)]
    tmp_count = 0
    tmp_m = m

    for stone in stones.pop(0):
        visited[stone[0]][stone[1]] = True
    for i in range(len(starts)):
        if not visited[starts[i][0]][starts[i][1]]:
            visited[starts[i][0]][starts[i][1]] = True
            q.append((starts[i][0],starts[i][1]))
            tmp_count+=1
        else:
            break
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if not grid [nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    tmp_count+=1
                elif  grid [nx][ny] and visited[nx][ny]:
                    if tmp_m:
                        tmp_m-=1
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        tmp_count+=1
                    else:
                        continue
    if max_count < tmp_count:
        max_count = tmp_count
print(max_count)
```
