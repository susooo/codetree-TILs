# 문제
https://www.codetree.ai/missions/2/problems/conveyor-belt-triangle?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 113ms <p>
Memory : 32MB

# 코드
```
n,t = map(int, input().split())
first_belt = list(map(int, input().split()))
second_belt = list(map(int, input().split()))
third_belt = list(map(int, input().split()))

belt = first_belt+second_belt+third_belt
for _ in range(t):
    temp = belt[-1]
    for i in range(3*n-1,0,-1):
        belt[i] = belt[i-1]
    belt[0] = temp

for i in belt[:n]:
    print(i, end=' ')
print()
for i in belt[n:2*n]:
    print(i, end=' ')
print()
for i in belt[2*n:]:
    print(i, end=' ')
```
