people = [x for x in map(int, input().split())]
count = [people[1]-people[0], people[2]-people[1]]
print(min(count)-1)
print(max(count)-1)