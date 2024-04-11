# 문제
https://www.codetree.ai/missions/2/problems/conveyor-belt?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 248ms <p>
Memory : 25MB

# 코드
```
n,t = map(int, input().split())
first_belt = list(map(int,input().split()))
second_belt = list(map(int,input().split()))
belt = first_belt+second_belt

for _ in range(t):
    temp = belt[-1]
    for j in range(2*n-1,0,-1):
        belt[j] = belt[j-1]
    belt[0] = temp

for i in belt[:n]:
    print(i, end=' ')
print()
for i in belt[n:]:
    print(i, end=' ')
```
