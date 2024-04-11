# 문제
https://www.codetree.ai/missions/2/problems/cross-shape-bomb?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 190ms <p>
Memory : 26MB

# 코드
```
from collections import deque
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
r,c = map(int,input().split())

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxs,dys = [0,1,0,-1],[1,0,-1,0]
count = grid[r-1][c-1]

#폭탄 터지기
x,y = r-1,c-1
grid[x][y] = 0
for i in range(1,count):
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx*i,y+dy*i
        if in_range(nx,ny):
            grid[nx][ny] = 0

final_grid = [[0]*n for _ in range(n)]
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(grid[j][i])

    #중력 작용하기
    temp2,temp3 = [], []
    for k in range(n):
        if temp[k]:
            temp2.append(temp[k])
    for k in range(n-len(temp2)):
        temp3.append(0)
    temp = temp3+temp2

    #최종 결과 완성하기
    for j in range(n):
        final_grid[j][i] = temp[j]

#출력하기
for i in range(n):
    for j in range(n):
        print(final_grid[i][j], end=' ')
    print()
```
