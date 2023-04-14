import itertools

with open("puzzle_input.txt", "r") as f:

    inputs = f.read().strip().splitlines()

calories = [sum(map(int, g)) for k, g in itertools.groupby(inputs, bool) if k]
        
# Part1

print(max(calories))

# Part2

calories.sort()

print(sum(calories[-3:]))