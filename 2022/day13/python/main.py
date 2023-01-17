distress = list(map(str.splitlines, open('puzzle_input.txt').read().strip().split("\n\n")))
packets = list(map(eval, open('puzzle_input.txt').read().split()))

def compare(x, y):
    
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compare([x], y)
    else:
        if type(y) == int:
            return compare(x, [y])
    
    for a, b in zip(x, y):
        result = compare(a, b)
        if result:
            return result
        
    return len(x) - len(y)

Sum = 0
i = 1
        
for (a, b) in distress:
    if compare(eval(a), eval(b)) < 0:
        Sum += i
    i += 1

key1 = 1
key2 = 2

for a in packets:
    if compare(a, [[2]]) < 0:
        key1 += 1
        key2 += 1
    elif compare(a, [[6]]) < 0:
        key2 += 1
        
print(Sum)
print(key1 * key2)
