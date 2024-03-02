people = [x for x in map(int, input().split())]

if people[1]-people[0]==1 and people[2]-people[1]==1:
    min_count = 0
elif people[1]-people[0]==2 or people[2]-people[1]==2:
    min_count = 1
else:
    min_count = 2

if people[1]-people[0]==1 and people[2]-people[1]==1:
    max_count = 0
else:
    max_count = max(people[1]-people[0],people[2]-people[1])-1
print(min_count)
print(max_count)