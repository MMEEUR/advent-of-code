import itertools

with open("puzzle_input.txt", "r") as f:

    inputs = f.read().strip().splitlines()

calories = [sum(map(int, g)) for k, g in itertools.groupby(inputs, bool) if k]
        
print(max(calories))
print(sum(sorted(calories)[-3:]))