from collections import deque

n,m,k = map(int,input().split())
direction = {1:(-1,0), 2:(1,0), 3:(0,1), 4:(0,-1)}
grid = [[0 for _ in range(m)] for _ in range(n)]
germ = deque()

def change_direction(x,y,d):
    if x==0 and d==1: d=2
    elif x==n-1 and d==2: d=1
    elif y==0 and d==4: d=3
    elif y==m-1 and d==3: d=4

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
        grid[x][y] = 0
        for _ in range(s):
            x,y,d = change_direction(x,y,d)
            dx,dy = direction[d]
            x,y = x+dx, y+dy

        if not grid[x][y]:
            grid[x][y] = (x,y,s,d,b)
        else:
            x2,y2,s2,d2,b2 = grid[x][y]
            grid[x][y] = compare((x,y,s,d,b), (x2,y2,s2,d2,b2))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                germ.append(grid[i][j])

def intern(j):
    global total
    x,y,s,d,b = -1,-1,-1,-1,-1
    for i in range(n):
        if grid[i][j]:
            x,y,s,d,b = grid[i][j]
            grid[i][j] = 0
            total += b
            break
    return x,y,s,d,b

total = 0
for _ in range(k):
    x,y,s,d,b = map(int, input().split())
    x-=1
    y-=1
    grid[x][y] = (x,y,s,d,b)
    germ.append((x,y,s,d,b))

for j in range(m):
    rx,ry,rs,rd,rb = intern(j)
    if rx != -1:
        germ.remove((rx,ry,rs,rd,rb))

    move_germ()

print(total)