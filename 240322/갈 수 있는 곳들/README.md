# 문제
https://www.codetree.ai/missions/2/problems/places-can-go?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 210ms <p>
Memory : 26MB

# 코드
```
from collections import deque

n,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
answer = 0

def bfs():
    global answer
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not graph[nx][ny] and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                answer += 1

q = deque()
for _ in range(k):
    r,c  = map(int, input().split())
    if not visited[r-1][c-1]:
        q.append((r-1,c-1))
        visited[r-1][c-1] = True
        answer += 1
        bfs()
print(answer)
```
