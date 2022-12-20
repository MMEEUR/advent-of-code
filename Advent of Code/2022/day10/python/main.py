Signals = open("puzzle_input.txt").read().splitlines()

X = 1
Cycle = 0
Strengths = []
Marked_signals = [20, 60, 100, 140, 180, 220]

for i in range(len(Signals)):
    signal = Signals[i]   
     
    if signal == "noop":
        Cycle += 1
        if Cycle in Marked_signals:
            Strengths.append(Cycle * X)
        
    else:      
        Cycle += 1
        if Cycle in Marked_signals:
            Strengths.append(Cycle * X)  
        Cycle += 1
        if Cycle in Marked_signals:
            Strengths.append(Cycle * X)
            
        X += int(signal.split()[1])
        
print("\n",sum(Strengths))

CRT = ["." for _ in range(240)]
X = 1
Cycle = 0

for i in range(len(Signals)):
    signal = Signals[i]
    
    if signal == "noop":
        pixel = (Cycle) % 40
        if abs(X - pixel) <= 1:
            CRT[Cycle % 240] = "█"
        else:
            CRT[Cycle % 240] = "."
        Cycle += 1
        
    else:
        pixel_x = Cycle % 40
        
        if abs(X - pixel_x) <= 1:
            CRT[Cycle % 240] = "█"
        else:
            CRT[Cycle % 240] = "."
            
        Cycle += 1
        
        pixel_x = Cycle % 40
        
        if abs(X - pixel_x) <= 1:
            CRT[Cycle % 240] = "█"
        else:
            CRT[Cycle % 240] = "."
            
        Cycle += 1
        
        X += int(signal.split()[1])
        
print("\n","\n".join("".join(CRT[i:i+40]) for i in range(0,240,40)))