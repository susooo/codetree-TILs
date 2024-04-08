# 문제
https://www.codetree.ai/missions/2/problems/make-one-using-four-operations?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 205ms <p>
Memory : 25MB

# 코드
```
from collections import deque
n = int(input())
q = deque()

def bfs():
    visited = set()
    while q:
        num,c = q.popleft()
        if num==1:
            return c
        if num in visited:
            continue
        visited.add(num)
        #4가지 연산
        q.append((num+1,c+1))
        q.append((num-1,c+1))
        if num%2==0:
            q.append((num//2,c+1))
        if num%3==0:
            q.append((num//3,c+1))

q.append((n,0))
print(bfs())
```
