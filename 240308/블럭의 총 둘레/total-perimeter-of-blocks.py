n = int(input())
r,c = [], []
for i in range(n):
    x,y = map(int, input().split())
    r.append(x)
    c.append(y)
print(2*(max(r)-min(r)+1)+2*(max(c)-min(c)+1))