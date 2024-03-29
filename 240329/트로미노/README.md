# 문제
https://www.codetree.ai/missions/2/problems/tromino?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 235ms <p>
Memory : 25MB

# 코드
```
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
tromino = [list(map(int,input().split())) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        d1 = [(-1,0),(0,1),(1,0),(0,-1),(-1,0)]
        d2 = [(0,-1),(0,1),(-1,0),(1,0)]
        #1번 블럭 회전시켜 모두 탐색
        for k in range(4):
            sum = tromino[i][j]
            b1x,b1y = i+d1[k][0], j+d1[k][1]
            b2x,b2y = i+d1[k+1][0], j+d1[k+1][1]
            if b1x<0 or b1x>=n or b1y<0 or b1y>=m or b2x<0 or b2x>=n or b2y<0 or b2y>=m:
                continue
            sum += tromino[b1x][b1y]
            sum += tromino[b2x][b2y]
            if sum > result:
                result = sum
        #2번 블럭 회전시켜 모두 탐색
        for k in range(0,4,2):
            sum = tromino[i][j]
            b1x,b1y = i+d2[k][0], j+d2[k][1]
            b2x,b2y = i+d2[k+1][0], j+d2[k+1][1]
            if b1x<0 or b1x>=n or b1y<0 or b1y>=m or b2x<0 or b2x>=n or b2y<0 or b2y>=m:
                continue
            sum += tromino[b1x][b1y]
            sum += tromino[b2x][b2y]
            if sum > result:
                result = sum
print(result)
```
