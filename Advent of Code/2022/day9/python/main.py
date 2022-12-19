input = open("puzzle_input.txt").read().splitlines()

positions = set([(0, 0)])
positions_2 = set([(0, 0)])

H = [0, 0]
T = [0, 0]

for a in range(len(input)):
    command = input[a]
    direction, steps = command.split()
    steps = int(steps)
    
    for b in range(steps):
        
        if direction == "R": x_axis = 1
        elif direction == "L": x_axis = -1
        else: x_axis = 0

        if direction == "U": y_axis = 1
        elif direction == "D": y_axis = -1
        else: y_axis = 0
        
        H[0] += x_axis
        H[1] += y_axis
        
        difference = [H[0] - T[0], H[1] - T[1]]
        
        if abs(difference[0]) > 1 or abs(difference[1]) > 1:
            
            if difference[0] == 0:
                T[1] += difference[1] // 2
        
            elif difference[1] == 0:
                T[0] += difference[0] // 2
                
            else:
                
                if difference[0] > 0 : T[0] += 1
                else: T[0] += -1
            
                if difference[1] > 0 : T[1] += 1
                else: T[1] += -1
                
        positions.add(tuple(T))

R = [[0, 0] for _ in range(10)]
H = [0, 0]
T = [0, 0]

for a in range(len(input)):
    command = input[a]
    direction, steps = command.split()
    steps = int(steps)
    
    for b in range(steps):
        
        if direction == "R": x_axis = 1
        elif direction == "L": x_axis = -1
        else: x_axis = 0

        if direction == "U": y_axis = 1
        elif direction == "D": y_axis = -1
        else: y_axis = 0
        
        R[0][0] += x_axis
        R[0][1] += y_axis
        
        for c in range(9): 
        
            H = R[c]
            T = R[c + 1]
            
            difference = [H[0] - T[0], H[1] - T[1]]
        
            if abs(difference[0]) > 1 or abs(difference[1]) > 1:
            
                if difference[0] == 0:
                    T[1] += difference[1] // 2
        
                elif difference[1] == 0:
                    T[0] += difference[0] // 2
                
                else:
                
                    if difference[0] > 0 : T[0] += 1
                    else: T[0] += -1
            
                    if difference[1] > 0 : T[1] += 1
                    else: T[1] += -1
                
        positions_2.add(tuple(R[-1]))   
                
print(len(positions))
print(len(positions_2))
