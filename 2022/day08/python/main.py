input = open("puzzle_input.txt")

input = input.read().splitlines()
trees = [list(map(int, line)) for line in input]

visible = 0
highest = 0

for i in range(len(trees)):
    
    for t in range(len(trees[i])):
        y = trees[i][t]
        
        if all(trees[i][x] < y for x in range(t)) or all(trees[i][x] < y for x in range(t + 1, len(trees[i]))) or all(trees[x][t] < y for x in range(i)) or all(trees[x][t] < y for x in range(i + 1, len(trees))):
            
            visible += 1

for i in range(len(trees)):
    
    for t in range(len(trees[i])):
        y = trees[i][t]
        
        UP = RIGHT = DOWN = LEFT = 0
        
        for x in range(i-1, -1, -1):
            UP += 1
            if y <= trees[x][t]:
                break
            
        for x in range(t+1, len(trees[i])):
            RIGHT += 1
            if y <= trees[i][x]:
                break
            
        for x in range(i+1, len(trees)):
            DOWN += 1
            if y <= trees[x][t]:
                break
            
        for x in range(t-1, -1, -1):
            LEFT += 1
            if y <= trees[i][x]:
                break
        
        highest = max(highest, UP * RIGHT * DOWN * LEFT)

print(visible)
print(highest)