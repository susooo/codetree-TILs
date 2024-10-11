from collections import deque

def change_direction(x,y,d):
    if d==1 and x==0: d=2
    elif d==2 and x==n-1: d=1
    elif d==4 and y==0: d=3
    elif d==3 and y==m-1: d=4

    return x,y,d
    
def compare(germ1, germ2):

    return germ1 if germ1[4] > germ2[4] else germ2

def move_germ():
    global germ

    while germ:
        x,y,s,d,b = germ.popleft()
        for _ in range(s):
            x,y,d = change_direction(x,y,d)
            dx,dy = direction[d]
            x,y = x+dx, y+dy

        if not grid[x][y]:
            grid[x][y] = (x,y,s,d,b)
        else:
            grid[x][y] = compare((x,y,s,d,b), grid[x][y])
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                germ.append(grid[i][j])
                grid[i][j] = 0

def intern(j):
    global total
    for i in range(n):
        if grid_germ[i][j]:
            x,y,s,d,b = grid_germ[i][j]
            grid_germ[i][j] = 0
            total += b
            return x,y,s,d,b
    return -1, -1, -1, -1, -1


n,m,k = map(int,input().split())
direction = {1:(-1,0), 2:(1,0), 3:(0,1), 4:(0,-1)}
grid = [[0]*m for _ in range(n)]
grid_germ = [[0]*m for _ in range(n)]
germ = deque()
total = 0

for _ in range(k):
    x,y,s,d,b = map(int, input().split())
    germ.append((x-1,y-1,s,d,b))

for j in range(m):
    for t in range(n):
        for k in range(m):
            grid_germ[t][k] = 0

    for tx,ty,ts,td,tb in germ:
        grid_germ[tx][ty] =  (tx,ty,ts,td,tb)

    rx,ry,rs,rd,rb = intern(j)
    if rx != -1:
        germ.remove((rx,ry,rs,rd,rb))

    move_germ()

print(total)