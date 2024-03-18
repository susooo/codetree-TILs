# 문제
[https://www.codetree.ai/missions/2/problems/best-place-of-33?&utm_source=clipboard&utm_medium=text](https://www.codetree.ai/missions/2/problems/seperate-village?&utm_source=clipboard&utm_medium=text)

# 복잡도
Time : 120ms <p>
Memory : 25MB

# 코드
```
n = int(input())
people = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
village = []

def dfs(x,y):
    global count
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if people[nx][ny] and not visited[nx][ny]:
            visited[nx][ny]=True
            count += 1
            dfs(nx,ny)
    return count

for i in range(n):
    for j in range(n):
        count = 0
        if people[i][j] and not visited[i][j]:
            visited[i][j]=True
            count += 1
            village.append(dfs(i,j))

print(len(village))
for v in sorted(village):
    print(v)
```
