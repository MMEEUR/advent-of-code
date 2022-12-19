input = open("puzzle_input.txt", "r")
total_elves_calories = input.read()
total_elves_calories = total_elves_calories.replace("\n", " ").replace("\n\n", "  ")

def puzzleSolver():
    
    split_elves = total_elves_calories.split("  ")
    total_elves = len(split_elves)
    elf_1st_calories = 0
    elf_2nd_calories = 0
    elf_3rd_calories = 0
    elf_3rd = 0
    elf_2nd = 0
    elf_1st = 0
    
    for i in range(total_elves):
        current_elf = split_elves[i]
        calories = current_elf.split(" ")
        int_calories = [eval(i) for i in calories]
        sum_calories = sum(int_calories)
        
        if elf_1st_calories < sum_calories:
            elf_2nd = elf_1st
            elf_1st = i
            elf_2nd_calories = elf_1st_calories
            elf_1st_calories = sum_calories
        
        if elf_1st_calories != sum_calories and elf_2nd_calories < sum_calories:
            elf_3rd = elf_2nd
            elf_2nd = i
            elf_3rd_calories = elf_2nd_calories
            elf_2nd_calories = sum_calories
            
        if elf_1st_calories != sum_calories and elf_2nd_calories != sum_calories and elf_3rd_calories < sum_calories:
            elf_3rd = i
            elf_3rd_calories = sum_calories
            
    print ("\nTop 3 Elves carrying the most Calories:\n")
    print ("\t Elf 1st: Number ",elf_1st," with ",elf_1st_calories,"Calories\n")
    print ("\t Elf 2nd: Number ",elf_2nd," with ",elf_2nd_calories,"Calories\n")
    print ("\t Elf 3rd: Number ",elf_3rd," with ",elf_3rd_calories,"Calories\n")
    print ("Total Top 3 Calories = ",elf_1st_calories + elf_2nd_calories + elf_3rd_calories)
    
puzzleSolver()
