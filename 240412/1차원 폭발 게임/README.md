# 문제
https://www.codetree.ai/missions/2/problems/The-1D-bomb-game?&utm_source=clipboard&utm_medium=text

# 복잡도
Time : 148ms <p>
Memory : 24MB

# 코드
```
n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]

while len(bombs) != len(set(bombs)):
    i = 0
    while i < len(bombs):
        if not bombs[i]:
            i += 1
            continue
        count = 1
        while i + count < len(bombs) and bombs[i] == bombs[i + count]:
            count += 1
        if count >= m:
            bombs[i:i + count] = [0] * count
        i += count
    # 중력 적용
    new_bombs = [bomb for bomb in bombs if bomb != 0]
    if len(new_bombs) == len(bombs):
        break
    bombs = new_bombs[:]

if m==1:
    print(0)
else:
    print(len(bombs))
    if len(bombs):
        for bomb in bombs:
            print(bomb)
```
