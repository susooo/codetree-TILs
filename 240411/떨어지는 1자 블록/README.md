# 문제
https://www.codetree.ai/missions/2/problems/falling-horizontal-block?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 127ms <p>
Memory : 25MB

# 코드
```
n,m,k = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

index = -1
for i in range(n):
    if 1 not in grid[i][k-1:k+m-1]:
        index = i
    else:
        break

if index!=-1:
    for j in range(k-1,k+m-1):
        grid[index][j] = 1
        
for row in grid:
    print(*row)
```
