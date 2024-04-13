n,m,p,c,d = map(int,input().split())
rr,rc = map(int,input().split())

pos = [(0,0) for _ in range(p+1)]
grid = [[0 for _ in range(n+1)] for _ in range(n+1)]
is_live = [False for _ in range(p+1)]
points = [0 for _ in range(p+1)]
stun = [0 for _ in range(p+1)]

for _ in range(p):
    id,sr,sc = map(int,input().split())

    grid[sr][sc] = id
    is_live[id] = True
    pos[id] = (sr,sc)

grid[rr][rc] = -1

dxs,dys = [-1,0,1,0],[0,1,0,-1]
def in_range(x,y):
    return 1<=x<n+1 and 1<=y<n+1

#step1) m번의 게임 수행
for t in range(1,m+1):
    #step2) 루돌프의 움직임
    closeX, closeY, closeIdx = 1000,1000,0
    for i in range(1,p+1):
        if not is_live[p]:
            continue
        currentBest = ((closeX-rr)**2+(closeY-rc)**2,(-closeX,-closeY))
        currentValue = ((pos[i][0]-rr)**2+(pos[i][1]-rc)**2,(-pos[i][0], -pos[i][1]))
        if currentValue <  currentBest:
            closeX,closeY = pos[i]
            closeIdx = i
    #가장 가까운 산타에게로 이동
    if closeIdx:
        prerudolf = (rr,rc)
        moveX = 0
        if closeX < rr:
            moveX = -1
        elif closeX > rr:
            moveX = 1

        moveY = 0
        if closeY < rc:
            moveY = -1
        elif closeY > rc:
            moveY = 1
        
        rr,rc = rr+moveX, rc+moveY
        grid[prerudolf[0]][prerudolf[1]] = 0

    #루돌프의 이동으로 충돌한 경우, 산타 이동 및 처리
    if closeX == rr and closeY == rc:
        firstX,firstY = closeX + moveX*c, closeY + moveY*c
        lastX,lastY = firstX, firstY
        stun[closeIdx] = t+1

        while in_range(lastX,lastY) and grid[lastX][lastY]>0:
            lastX += moveX
            lastY += moveY
        
        while not (lastX == firstX and lastY == firstY):
            beforeX = lastX - moveX
            beforeY = lastY - moveY

            if not in_range(beforeX, beforeY):
                break
            
            idx = grid[beforeX][beforeY]
            if not in_range(lastX, lastY):
                is_live[idx] = False
            else:
                grid[lastX][lastY] = grid[beforeX][beforeY]
                pos[idx] = (lastX,lastY)

            lastX,lastY = beforeX, beforeY
        
        points[closeIdx] += c
        pos[closeIdx] = (firstX, firstY)
        if in_range(firstX, firstY):
            grid[firstX][firstY] = closeIdx
        else:
            is_live[closeIdx] = False
    
    grid[rr][rc] = -1

    #step3) 산타의 움직임
    for i in range(1,p+1):
        if not is_live[i]:
            continue
        
        minDist = (pos[i][0]-rr)**2 + (pos[i][1]-rc)**2
        moveDir = -1

        for dir in range(4):
            nx,ny = pos[i][0]+dxs[dir], pos[i][1]+dys[dir]

            if not in_range(nx,ny) or grid[nx][ny]>0:
                continue
            
            dist = (nx-rr)**2 + (ny-rc)**2
            if dist < minDist:
                minDist = dist
                moveDir = dir

        if moveDir != -1:
            nx,ny = pos[i][0]+dxs[moveDir], pos[i][1]+dys[moveDir]

            #step3) 산타의 이동으로 충돌한 경우, 산타 이동 및 처리
            if nx==rr and ny==rc:
                moveX = -dxs[moveDir]
                moveY = -dys[moveDir]

                firstX,firstY = nx + moveX*d, ny + moveY*d
                lastX,lastY = firstX, firstY
                stun[closeIdx] = t+1

                if d == 1:
                    points[i] += 1
                else:
                    while in_range(lastX,lastY) and grid[lastX][lastY]>0:
                        lastX += moveX
                        lastY += moveY
                    
                    while lastX != firstX or lastY != firstY:
                        beforeX = lastX - moveX
                        beforeY = lastY - moveY

                        if not in_range(beforeX, beforeY):
                            break
                        
                        idx = grid[beforeX][beforeY]
                        if not in_range(lastX, lastY):
                            is_live[idx] = False
                        else:
                            grid[lastX][lastY] = grid[beforeX][beforeY]
                            pos[idx] = (lastX,lastY)

                        lastX,lastY = beforeX, beforeY
                    
                    points[i] += d
                    grid[pos[i][0]][pos[i][1]] = 0
                    pos[i] = (firstX, firstY)
                    if in_range(firstX, firstY):
                        grid[firstX][firstY] = i
                    else:
                        is_live[i] = False
            else:
                grid[pos[i][0]][pos[i][1]] = 0
                pos[i] = (nx,ny)
                grid[nx][ny] = i
    
    #턴이 지나고 탈락하지 않은 산타들의 점수를 1 증가
    for i in range(1, p+1):
        if is_live[i]:
            points[i] += 1

# 결과 출력
for i in range(1, p + 1):
    print(points[i], end=" ")