with open("puzzle_input.txt") as f:

    inputs = f.read().splitlines()
    
inputs = [line.strip().split() for line in inputs]
inputs = [(ord(a) - 64, ord(b) - 87) for a, b in inputs]
    
def solver(a: int, b: int, part: bool) -> int:
    
    if part:  
        return b + 3 if a == b else b + 6 if (b - a) % 3 == 1 else b
    
    else:
        return (a - 2) % 3 + 1 if b == 1 else a + 3 if b == 2 else a % 3 + 7
  
print(sum(solver(a, b, True) for a, b in inputs))
print(sum(solver(a, b, False) for a, b in inputs))