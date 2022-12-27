input = open("puzzle_input.txt", "r")

commands = input.read().strip().splitlines()
files = {}
folders = set()
dirs = []

for c in commands:
    if c.startswith("$"):
        
        if c.startswith("$ cd"):
            root = c[5:]
            
            if root == "..":
                if len(dirs) > 0:
                    dirs.pop()
            
            elif root == "/":
                dirs = []
                
            else:
                dirs.extend(root.split("/"))
                
    else:
        size, name = c.split(" ")
        
        if size != "dir":
            size = int(size)
            files["/".join(dirs + [name])] = size
    
    folders.add("/".join(dirs))
    
sum_size = 0

fsizes = {}

for folder in folders:
    fsize = 0
    
    for file in files:
        
        if file.startswith(folder):
            fsize += files[file]
            
    if fsize <= 100000:
        sum_size += fsize
        
    fsizes[folder] = fsize

print(sum_size)

print(min(i for i in fsizes.values() if 70000000 - fsizes[""] + i >= 30000000))