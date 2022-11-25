with open('day1.txt') as f:
    lines = [line.rstrip() for line in f]

number_list = [int(i) for a, i in enumerate(lines[0])]
part2_list = number_list + number_list

part1 = 0
part2 = 0

for i in range(len(number_list) - 1):
    if number_list[i] == number_list[i + 1]:
        part1 += number_list[i]

if number_list[0] == number_list[-1]:
    part1 += number_list[0]

for i in range(len(number_list)):
    nl = int(len(number_list) / 2 + i)
    if part2_list[i] == part2_list[nl]:
        part2 += number_list[i]


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

