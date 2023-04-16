from typing import List, Tuple

with open("puzzle_input.txt") as f:

    inputs: List[Tuple[int, int]] = [tuple((ord(line.split()[0]) - 64, ord(line.split()[1]) - 87)) for line in f.read().splitlines()]
    
def solver(a: int, b: int, part: bool) -> int:
    
    if part:  
        return b + 3 if a == b else b + 6 if (b - a) % 3 == 1 else b
    
    else:
        return (a - 2) % 3 + 1 if b == 1 else a + 3 if b == 2 else a % 3 + 7
  
print(sum(solver(a, b, True) for a, b in inputs))
print(sum(solver(a, b, False) for a, b in inputs))