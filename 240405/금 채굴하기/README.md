# 문제
https://www.codetree.ai/missions/2/problems/gold-mining?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 368ms <p>
Memory : 29MB

# 코드
```
from collections import deque
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y]

def bfs():
    dxs,dys = [0,1,0,-1],[1,0,-1,0]
    global gold, gold_count, final_gold
    expansion = 0

    while q:
        x,y,index = q.popleft()
        cost = index**2 + (index+1)**2
        if index > 2*n-1:
            return final_gold
        #마름모 확장
        if expansion != index:
            expansion = index
            if gold-cost>=0:
                if final_gold<gold_count:
                    final_gold=gold_count
        #마름모 탐색
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny,index+1))
                #최대 금 개수
                if grid[nx][ny]:
                    gold+=m
                    gold_count+=1
    return  final_gold
               
final_gold_count = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            gold, gold_count, final_gold = m,1,1
        else:
            gold, gold_count, final_gold = 0,0,0
        visited = [[False]*n for _ in range(n)]
        q = deque()
        visited[i][j] = True
        q.append((i,j,0))

        tmp_gold_count = bfs()
        if final_gold_count < tmp_gold_count:
            final_gold_count = tmp_gold_count
print(final_gold_count)
```
