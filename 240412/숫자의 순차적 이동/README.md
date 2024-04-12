# 문제
https://www.codetree.ai/missions/2/problems/sequential-movement-of-numbers?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 237ms <p>
Memory : 27MB

# 코드
```
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y, max_value):
    return in_range(x,y) and grid[x][y]>max_value

def simulate(x,y):
    dxs,dys = [0,1,0,-1,-1,1,1,-1],[1,0,-1,0,1,1,-1,-1]
    max_x,max_y,max_value = 0,0,0
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx,y+dy
        if can_go(nx,ny,max_value):
            max_x,max_y,max_value = nx,ny,grid[nx][ny]
    return max_x,max_y

while m:
    for index in range(1, n * n + 1):
        found = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == index:
                    x, y = r, c
                    found = True
                    break
            if found:
                break
        s_x,s_y = simulate(x,y)
        tmp = grid[s_x][s_y]
        grid[s_x][s_y] = grid[x][y]
        grid[x][y] = tmp
    m-=1

for r in range(n):
    for c in range(n):
        print(grid[r][c], end=' ')
    print()
```
