import itertools

inputs = open("puzzle_input.txt", "r").read().strip().splitlines()

calories = [sum(map(int, g)) for k, g in itertools.groupby(inputs, bool) if k]
        
# Part1

print(max(calories))

# Part2

calories.sort()

print(sum(calories[-3:]))