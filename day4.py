from collections import Counter

with open('day4.txt') as f:
    lines = [line.rstrip() for line in f]

part1 = 0
for line in lines:
    c = dict(Counter(line.split(" ")))
    for x in c.values():
        if x > 1:
            break
    else:
        part1 += 1

for line in lines:
    c = dict(Counter(line.split(" ")))
    for p2 in list(c):
        print(p2)
        print(Counter(p2).most_common())
    print("-"*20)
# print(part1)
