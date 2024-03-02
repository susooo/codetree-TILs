people = [x for x in map(int, input().split())]

if people[1]-people[0]==1 and people[2]-people[1]==1:
    min_count = 0
elif people[1]-people[0]==1:
    min_count = (people[2]-people[1])//2
elif people[2]-people[1]==1:
    min_count = (people[1]-people[0]-1)//2
else:
    min_count = min(people[1]-people[0],people[2]-people[1])-1

if people[1]-people[0]==1 and people[2]-people[1]==1:
    max_count = 0
elif people[1]-people[0]==1:
    max_count = people[2]-people[1]-1
elif people[2]-people[1]==1:
    max_count = people[1]-people[0]-1
else:
    max_count = max(people[1]-people[0],people[2]-people[1])-1
print(min_count)
print(max_count)