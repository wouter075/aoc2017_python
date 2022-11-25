with open('day2.txt') as f:
    lines = [line.rstrip() for line in f]

sheet = []
part1 = 0
part2 = 0
for line in lines:
    sheet.append([int(x) for x in line.split("\t")])
    # sheet.append([int(x) for x in line.split(" ")])

for row in sheet:
    part1 += abs(max(row) - min(row))

for r in range(len(sheet)):
    for x in range(len(sheet[r])):
        for y in range(len(sheet[r])):
            if sheet[r][x] != sheet[r][y]:
                if (sheet[r][x] / sheet[r][y]).is_integer():
                    part2 += int(sheet[r][x] / sheet[r][y])


print(part1)
print(part2)
