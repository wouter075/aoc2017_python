from collections import Counter

with open('day4.txt') as f:
    lines = [line.rstrip() for line in f]

part1 = 0
part2 = 0
for line in lines:
    c = dict(Counter(line.split(" ")))
    for x in c.values():
        if x > 1:
            break
    else:
        part1 += 1

        # for part 2
        anagram = False
        anagram_list = []
        for p2 in list(c):
            anagram_list.append(sorted(Counter(p2).most_common()))

        for x in range(0, len(anagram_list)):
            for y in range(0, len(anagram_list)):
                if x != y:
                    if anagram_list[x] == anagram_list[y]:
                        anagram = True
                        break
        if anagram:
            print(f'[Not valid] {line}')
        else:
            print(f'[Valid] {line}')
            part2 += 1

print(part1)
print(part2)
