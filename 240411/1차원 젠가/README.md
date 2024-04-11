# 문제
https://www.codetree.ai/missions/2/problems/jenga-1d?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 104ms <p>
Memory : 24MB

# 코드
```
n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int,input().split())
s2, e2 = map(int,input().split())

temp = blocks[:]
temp2, temp3 = [], []
#1번 블록 빼기
for i in range(s1-1,e1):
    temp[i] = 0
for i in temp:
    if i:
        temp2.append(i)
#2번 블록 빼기
for j in range(s2-1,e2):
    temp2[j] = 0
for j in temp2:
    if j:
        temp3.append(j)
#출력
if temp3:
    print(len(temp3))
    while temp3:
        print(temp3.pop(0))
else:
    print(0)
```
