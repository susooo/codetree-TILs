from collections import deque

def change_direction(x,y,d):
    if d==1 and x==0: d=2
    elif d==2 and x==n-1: d=1
    elif d==4 and y==0: d=3
    elif d==3 and y==m-1: d=4

    return x,y,d
    
def compare(germ1, germ2):
    x1,y1,s1,d1,b1 = germ1
    x2,y2,s2,d2,b2 = germ2

    if b1 > b2: return (x1,y1,s1,d1,b1)
    else: return (x2,y2,s2,d2,b2)

def move_germ():
    global germ

    while germ:
        x,y,s,d,b = germ.popleft()
        for _ in range(s):
            nx,ny,d = change_direction(x,y,d)
            dx,dy = direction[d]
            x,y = nx+dx, ny+dy

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
    x,y,s,d,b = -1,-1,-1,-1,-1
    for i in range(n):
        if grid_germ[i][j]:
            x,y,s,d,b = grid_germ[i][j]
            grid_germ[i][j] = 0
            total += b
            break
    return x,y,s,d,b

n,m,k = map(int,input().split())
direction = {1:(-1,0), 2:(1,0), 3:(0,1), 4:(0,-1)}
grid = [[0 for _ in range(m)] for _ in range(n)]
germ = deque()
total = 0

for _ in range(k):
    x,y,s,d,b = map(int, input().split())
    x,y = x-1,y-1
    germ.append((x,y,s,d,b))

for j in range(m):
    grid_germ = [[0 for _ in range(m)] for _ in range(n)]
    for tx,ty,ts,td,tb in germ:
        grid_germ[tx][ty] =  (tx,ty,ts,td,tb)

    rx,ry,rs,rd,rb = intern(j)
    if rx != -1:
        germ.remove((rx,ry,rs,rd,rb))

    move_germ()

print(total)