input = open("puzzle_input.txt","r")

instructions = input.read().splitlines()

stacks = [
    [],
    list("CZNBMWQV"),
    list("HZRWCB"),
    list("FQRJ"),
    list("ZSWHFNMT"),
    list("GFWLNQP"),
    list("LPW"),
    list("VBDRGCQJ"),
    list("ZQNBW"),
    list("HLFCGTJ"),
]

for i in instructions[10:]:
    current_command = i[5:]
    c1, s, = current_command.split(" from ")
    c2, c3 = s.split(" to ")
    c1,c2,c3 = int(c1), int(c2), int(c3)
    
    for _ in range(c1):
        stacks[c3].append(stacks[c2].pop(-1))
        
print("".join(top[-1] for top in stacks[1:]))

stacks = [
    [],
    list("CZNBMWQV"),
    list("HZRWCB"),
    list("FQRJ"),
    list("ZSWHFNMT"),
    list("GFWLNQP"),
    list("LPW"),
    list("VBDRGCQJ"),
    list("ZQNBW"),
    list("HLFCGTJ"),
]

for i in instructions[10:]:
    current_command = i[5:]
    c1, s, = current_command.split(" from ")
    c2, c3 = s.split(" to ")
    c1,c2,c3 = int(c1), int(c2), int(c3)
    
    stacks[c3].extend(stacks[c2][-c1:])
    del stacks[c2][-c1:]
        
print("".join(top[-1] for top in stacks[1:]))
