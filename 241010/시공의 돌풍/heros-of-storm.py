dxs, dys = [0,1,0,-1], [1,0,-1,0]
def in_range(x,y):
    if 0<=x<n and 0<=y<m:
        if dusts[x][y] == -1: return False
        else: return True
    else: return False

def move_dust():
    global grid

    for i in range(n):
        for j in range(m):
            count = 0
            plus_dust = 0
            if dusts[i][j] != -1:
                for k in range(4):
                    dx,dy = i+dxs[k], j+dys[k]
                    if in_range(dx,dy):
                        count += 1
                        plus_dust += dusts[dx][dy]//5
                minus_dust = dusts[i][j]//5
                grid[i][j] = dusts[i][j] - minus_dust*count + plus_dust
            else:
                grid[i][j] = -1
    return grid
    
cx1,cy1 = [-1,0,1,0], [0,1,0,-1]
cx2,cy2 = [1,0,-1,0], [0,1,0,-1]
def move_cleaner():
    global storm
    r1, c1 = storm[0]
    r2, c2 = storm[1]
    count = [r1,m-1,r1,m-1]
    br1,bc1 = r1,c1
    br2,bc2 = r2,c2

    for k in range(4):
        for _ in range(count[k]):
            dx1,dy1 = br1+cx1[k], bc1+cy1[k]
            if dusts[br1][bc1] != -1:
                dusts[br1][bc1] = dusts[dx1][dy1]
            if dusts[dx1][dy1] == -1:
                dusts[br1][bc1] = 0
            br1,bc1 = dx1,dy1

        for _ in range(count[k]):
            dx2,dy2 = br2+cx2[k], bc2+cy2[k]
            if dusts[br2][bc2] != -1:
                dusts[br2][bc2] = dusts[dx2][dy2]
            if dusts[dx2][dy2] == -1:
                dusts[br2][bc2] = 0
            br2,bc2 = dx2,dy2
    return dusts
    
n,m,t = map(int,input().split())
dusts = []
for _ in range(n):
    dust = list(map(int, input().split()))
    dusts.append(dust)

storm = []
for i in range(n):
    for j in range(m):
        if dusts[i][j] == -1:
            storm.append((i,j))

for _ in range(t):
    grid = [[0 for _ in range(m)] for _ in range(n)]
    dusts = move_dust()

    dusts = move_cleaner()

total_sum = sum(sum(row) for row in dusts)
print(total_sum+2)