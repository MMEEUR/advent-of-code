from collections import deque

puzzle_input = open('puzzle_input.txt').read().strip().splitlines()

indices = {}
valves = {}
tunnels = {}
distances = {}
have_pressure = []
cache = {}

for line in puzzle_input:
    line = line.strip()
    valve = line.split()[1]
    flow = int(line.split(";")[0].split("=")[1])
    targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
    valves[valve] = flow
    tunnels[valve] = targets

for valve in valves:
    if valve != "AA" and valves[valve] == 0:
        continue
    
    if valve != "AA":
        have_pressure.append(valve)

    distances[valve] = {valve: 0, "AA": 0}
    visited = {valve} 
    queue = deque([(0, valve)])
    
    while queue:
        distance, position = queue.popleft()
        
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            
            visited.add(neighbor)
            
            if valves[neighbor]:
                distances[valve][neighbor] = distance + 1
                
            queue.append((distance + 1, neighbor))

    del distances[valve][valve]
    if valve != "AA":
        del distances[valve]["AA"]

for index, element in enumerate(have_pressure):
    indices[element] = index

def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]
    
    maxval = 0
    
    for neighbor in distances[valve]:
        bit = 1 << indices[neighbor]
        
        if bitmask & bit:
            continue
        
        remtime = time - distances[valve][neighbor] - 1
        
        if remtime <= 0:
            continue
        
        maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime)
        
    cache[(time, valve, bitmask)] = maxval
    
    return maxval

b = (1 << len(have_pressure)) - 1
m = 0

for i in range((b + 1) // 2):
    m = max(m, dfs(26, "AA", i) + dfs(26, "AA", b ^ i))

print(dfs(30, "AA", 0))
print(m)