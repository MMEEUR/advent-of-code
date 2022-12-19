rucksacks = open("puzzle_input.txt").read().splitlines()
rucksacks2 = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

def puzzleSolver():
    priorities = 0
    
    for i in range(len(rucksacks)):
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
    priorities = 0
    
    for i in range(len(rucksacks2)):
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
