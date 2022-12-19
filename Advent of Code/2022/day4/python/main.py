elves_groups = open("puzzle_input.txt").read().splitlines()
futilities = 0
overlaps = 0

for i in range(len(elves_groups)):
    current_group = elves_groups[i].split(",")
    elf1 = [eval(i) for i in (current_group[0].split("-"))]
    elf2 = [eval(i) for i in (current_group[1].split("-"))]
    
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1] or elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
        futilities += 1
        
    if set(range(elf1[0], elf1[1]+1)) & set(range(elf2[0], elf2[1]+1)):
        overlaps += 1
        
print("futilities:\t",futilities)
print("overlaps:\t",overlaps)
