# 문제
https://www.codetree.ai/missions/2/problems/move-to-max-k-times?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 429ms <p>
Memory : 28MB

# 코드
```
from collections import deque

n,k = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
r,c = map(int, input().split())

def check():
    global k_r, k_c
    for i in range(4):
        check_r = k_r+dx[i]
        check_c = k_c+dy[i]
        if check_r<0 or check_r>=n or check_c<0 or check_c>=n or n_list[check_r][check_c]>=n_list[k_r][k_c]:
            continue
        else:
            return True
    return False

q = deque()
max_r, max_c = r-1,c-1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

while k:
    visited = [[False]*n for _ in range(n)]
    k_num,k_r, k_c = 0,max_r, max_c
    visited[k_r][k_c] = True
    q.append((k_r, k_c))
    if not check():
        break
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n or n_list[nx][ny]>=n_list[k_r][k_c]:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                if k_num < n_list[nx][ny]:
                    k_num = n_list[nx][ny]
                    max_r, max_c = nx, ny
                elif k_num == n_list[nx][ny]:
                    if max_r > nx:
                        max_r, max_c = nx, ny
                    elif max_r == nx and max_c > ny:
                        max_r, max_c = nx, ny
    k-=1
print(max_r+1, max_c+1)
```
