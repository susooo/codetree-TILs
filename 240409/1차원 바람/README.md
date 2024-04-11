# 문제
https://www.codetree.ai/missions/2/problems/The-1D-wind-blows?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 213ms <p>
Memory : 28MB

# 코드
```
from collections import deque
n,m,q = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
wind = [list(input().split()) for _ in range(q)]

def in_range(x):
    return 0<=x and x<n

def effect(r,d):
    #해당 행 바람 불기
    if d=='R':
        temp = grid[r][0]
        for i in range(m-1):
            grid[r][i] = grid[r][i+1]
        grid[r][-1] = temp
    else:
        temp = grid[r][-1]
        for i in range(m-1,0,-1):
            grid[r][i] = grid[r][i-1]
        grid[r][0] = temp

def can_windy(r,d):
    effect(r,d)
    new_d = 'R' if d=='L' else 'L'
    up_d,down_d = new_d, new_d
    #바람 영향주기
    while up:
        rx = up.popleft()
        if in_range(rx) and in_range(rx-1):
            #같은 열에 같은 숫자가 적힌 경우 1이상
            for i in range(m):
                if grid[rx][i] == grid[rx-1][i]:
                    effect(rx-1, up_d)
                    up_d = 'R' if up_d=='L' else 'L'
                    up.append(rx-1)
                    break
    while down:
        rx = down.popleft()
        if in_range(rx) and in_range(rx+1):
            #같은 열에 같은 숫자가 적힌 경우 1이상
            for i in range(m):
                if grid[rx][i] == grid[rx+1][i]:
                    effect(rx+1, down_d)
                    down_d = 'R' if down_d=='L' else 'L'
                    down.append(rx+1)
                    break

for i in range(len(wind)):
    r = int(wind[i][0])
    d = wind[i][1]
    up, down = deque(), deque()
    up.append(r-1)
    down.append(r-1)
    can_windy(r-1,d)
        
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
```
