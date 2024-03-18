# 문제
[https://www.codetree.ai/missions/2/problems/best-place-of-33?&utm_source=clipboard&utm_medium=text](https://www.codetree.ai/missions/2/problems/determine-escapableness-with-2-ways?&utm_source=clipboard&utm_medium=text)

# 복잡도
Time : 138ms <p>
Memory : 27MB

# 코드
```
n,m = map(int, input().split())
snake = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def dfs(x,y):
    dx = [0,1]
    dy = [1,0]

    for i in range(2):
        nx = dx[i]+x
        ny = dy[i]+y
        if nx<n and ny<m and snake[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx,ny)
dfs(0,0)
print(1) if visited[n-1][m-1] else print(0)
```
