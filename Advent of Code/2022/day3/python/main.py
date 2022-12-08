input = open("puzzle_input.txt", "r")

rucksacks = input.read().split("\n")
rucksacks2 = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

def puzzleSolver():
    total_rucksacks = len(rucksacks)
    priorities = 0
    
    for i in range(total_rucksacks):
        current_rucksack = rucksacks[i]
        length = len(current_rucksack) // 2
        current_rucksack1 = current_rucksack[:length]
        current_rucksack2 = current_rucksack[length:]
        common_word, = set(current_rucksack1) & set(current_rucksack2)
        
        if common_word >= "a":
            priorities += ord(common_word) - ord("a") + 1
        else:
            priorities += ord(common_word) - ord("A") + 27
            
    print(priorities)
    
def puzzleSolver2():
    total_rucksacks = len(rucksacks2)
    priorities = 0
    
    for i in range(total_rucksacks):
        current_rucksack = rucksacks2[i]
        current_rucksack1 = current_rucksack[0]
        current_rucksack2 = current_rucksack[1]
        current_rucksack3 = current_rucksack[2]

        common_word, = set(current_rucksack1) & set(current_rucksack2) & set(current_rucksack3)
        
        if common_word >= "a":
            priorities += ord(common_word) - ord("a") + 1
        else:
            priorities += ord(common_word) - ord("A") + 27

    print(priorities)
    
puzzleSolver()
puzzleSolver2()