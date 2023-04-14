with open("puzzle_input.txt") as f:
    inputs = f.read().splitlines()
    
def solver(part: bool, a: str, b: str = None, c: str = None) -> int:
    
    if part:
        
        x: int = len(a) // 2
        
        common, = set(a[x:]) & set(a[:x])
        
        return ord(common) - 96 if common >= "a" else ord(common) - 38
        
    else:
        
        common, = set(a) & set(b) & set(c)
        
        return ord(common) - 96 if common >= "a" else ord(common) - 38

print(sum(solver(True, a) for a in inputs))
print(sum(solver(False, *inputs[i:i+3]) for i in range(0, len(inputs), 3)))