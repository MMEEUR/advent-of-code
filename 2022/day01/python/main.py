import itertools
from typing import List

with open("puzzle_input.txt", "r") as f:

    calories: List[str] = f.read().strip().splitlines()

calories: List[int] = [sum(map(int, g)) for k, g in itertools.groupby(calories, bool) if k]
        
print(max(calories))
print(sum(sorted(calories)[-3:]))