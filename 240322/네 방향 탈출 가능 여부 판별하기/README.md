# 문제
[https://www.codetree.ai/missions/2/problems/best-place-of-33?&utm_source=clipboard&utm_medium=text](https://www.codetree.ai/missions/2/problems/determine-escapableness-with-4-ways?&utm_source=clipboard&utm_medium=text)

# 복잡도
Time : 174ms <p>
Memory : 25MB

# 코드
```
from collections import deque

n,m = map(int, input().split())
snakes = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs():
    global available
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if snakes[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True 
                q.append((nx,ny))
    print(1) if visited[n-1][m-1] == True else print(0)
        
q=deque()
q.append((0,0))
visited[0][0] = True
bfs()
```
