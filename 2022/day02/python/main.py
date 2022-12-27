input = open("puzzle_input.txt").read().splitlines()

def puzzleSolver1():
    total_score = 0
    
    for i in range(len(input)):
        current_round = input[i].split(" ")
        
        if current_round[0] == 'A' and current_round[1] == 'X': total_score += 4
            
        if current_round[0] == 'A' and current_round[1] == 'Y': total_score += 8
            
        if current_round[0] == 'A' and current_round[1] == 'Z': total_score += 3
                
        if current_round[0] == 'B' and current_round[1] == 'X': total_score += 1
                
        if current_round[0] == 'B' and current_round[1] == 'Y': total_score += 5
                
        if current_round[0] == 'B' and current_round[1] == 'Z': total_score += 9
            
        if current_round[0] == 'C' and current_round[1] == 'X': total_score += 7
                
        if current_round[0] == 'C' and current_round[1] == 'Y': total_score += 2
                
        if current_round[0] == 'C' and current_round[1] == 'Z': total_score += 6
           
    print("Puzzle Part 1 ----------- Total game score:\t",total_score)
    
def puzzleSolver2():
    total_score = 0
    
    for i in range(len(input)):
        current_round = input[i].split(" ")
        
        if current_round[0] == 'A' and current_round[1] == 'X': total_score += 3
            
        if current_round[0] == 'A' and current_round[1] == 'Y': total_score += 4
            
        if current_round[0] == 'A' and current_round[1] == 'Z': total_score += 8
                
        if current_round[0] == 'B' and current_round[1] == 'X': total_score += 1
                
        if current_round[0] == 'B' and current_round[1] == 'Y': total_score += 5
                
        if current_round[0] == 'B' and current_round[1] == 'Z': total_score += 9
            
        if current_round[0] == 'C' and current_round[1] == 'X': total_score += 2
                
        if current_round[0] == 'C' and current_round[1] == 'Y': total_score += 6
                
        if current_round[0] == 'C' and current_round[1] == 'Z': total_score += 7
           
    print("Puzzle Part 2 ----------- Total game score:\t",total_score)
    
puzzleSolver1()
puzzleSolver2()