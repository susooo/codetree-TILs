n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

blocks = [[(0,1),(0,2),(0,3)],[(0,1),(1,1),(1,0)],[(-1,0),(0,1),(1,1)],[(-1,0),(0,1),(1,0)],[(-1,0),(1,0),(1,1)]]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    return in_range(x,y) and not visited[x][y]

def search(x,y):
    max_sum = 0

    for block in blocks:
        sum = grid[x][y]

        for dx, dy in block:
            nx,ny = x+dx,y+dy
            if in_range(nx,ny):
                sum += grid[nx][ny]
        max_sum = max(max_sum,sum) 
    return max_sum

final_sum = 0
for i in range(n):
    for j in range(m):
        final_sum = max(final_sum,search(i,j))
print(final_sum)