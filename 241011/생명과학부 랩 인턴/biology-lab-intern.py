n,m,k = map(int,input().split())

#0이 위, 1이 아래, 2가 오른쪽, 3이 왼쪽
direction = [(-1,0), (1,0), (0,1), (0,-1)]
directions_oppo = [1,0,3,2]

grid = [[0]*m for _ in range(n)]
info = dict()
answer = 0

for _ in range(k):
    x,y,s,d,b = map(lambda x:int(x)-1, input().split())
    grid[x][y] = b+1
    info[b+1] = [x,y,s+1,d]


for j in range(m):
    # 채취
    for i in range(n):
        if grid[i][j]:
            answer += grid[i][j]
            info.pop(grid[i][j])
            break

    new_grid = [[0]*m for _ in range(n)]
    new_info = dict()

    # 곰팡이 이동
    for size, (x,y,s,d) in sorted(info.items(), key=lambda x: (-x[0])):
        dx,dy = direction[d]
        nx,ny = x, y
        for _ in range(s):
            nx,ny = nx+dx, ny+dy 
            if not (0<=nx<n and 0<=ny<m):
                nx,ny = nx-dx, ny-dy
                d = directions_oppo[d]
                dx,dy = direction[d]
                nx,ny = nx+dx, ny+dy
            
        if not new_grid[nx][ny]:
            new_grid[nx][ny] = size
            new_info[size] = [nx,ny,s,d]
    
    grid = new_grid
    info = new_info

    if not info:
        break

print(answer)