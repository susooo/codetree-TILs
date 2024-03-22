# 문제
[https://www.codetree.ai/missions/2/problems/best-place-of-33?&utm_source=clipboard&utm_medium=text](https://www.codetree.ai/missions/2/problems/puyo-puyo?&utm_source=clipboard&utm_medium=text)

# 복잡도
Time : 149ms <p>
Memory : 26MB

# 코드
```
n = int(input())
blocks = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
popped_blocks = 0
max_blocks = 0

def dfs(k,x,y):
    global count
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if blocks[nx][ny] == k and not visited[nx][ny]:
            visited[nx][ny] = True
            count += 1
            dfs(k, nx,ny)
    return count

for i in range(n):
    for j in range(n):
        count = 0
        if not visited[i][j]:
            visited[i][j] = True
            count+=1
            count=dfs(blocks[i][j],i,j)
            if max_blocks < count:
                max_blocks = count
            if count >=4:
                popped_blocks+=1
print(popped_blocks, max_blocks)
```
