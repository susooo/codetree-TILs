# 문제
https://www.codetree.ai/missions/2/problems/best-place-of-33?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 124ms <p>
Memory : 25MB

# 코드
```
n = int(input())
graph = []
result = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

def search(x, y):
    tmp = 0
    global result
    if (y+2)>=n:
        search(x+1, 0)
    elif (x+2)>=n:
        print(result)
    else:
        for i in range(x, x+3):
            for j in range(y, y+3):
                if graph[i][j]:
                    tmp += 1
        if tmp > result:
            result = tmp
        search(x, y+1)
search(0,0)
```
