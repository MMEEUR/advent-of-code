import re
from typing import List

with open("puzzle_input.txt") as f:
    
    inputs: List[List[int]] = [map(int, re.findall('\d+', x,)) for x in f.read().splitlines()]
    
futilities: int = 0
overlaps: int = 0

for a, b, c, d in inputs:
    
    if a <= c and b >= d or c <= a and d >= b:
        futilities += 1
        
    if set(range(a, b+1)) & set(range(c, d+1)):
        overlaps += 1
      
print(futilities)
print(overlaps)