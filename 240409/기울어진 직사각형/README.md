# 문제
https://www.codetree.ai/missions/2/problems/slanted-rectangle?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 240ms <p>
Memory : 26MB

# 코드
```
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def get_score(x,y,k,l):
    dxs,dys = [-1,-1,1,1],[1,-1,-1,1]
    move_nums =  [k,l,k,l]
    sum_of_nums = 0

    for dx,dy,move_num in zip(dxs,dys, move_nums):
        for _ in range(move_num):
            x,y = x+dx, y+dy
            if not in_range(x,y):
                return 0
            sum_of_nums += grid[x][y]
    return sum_of_nums

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(1,n):
            for l in range(1,n):
                ans = max(ans, get_score(i,j,k,l))

print(ans)
```
