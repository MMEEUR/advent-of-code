input = open("puzzle_input.txt", "r")

signals = list(input.read())

for i in range(len(signals)-3):  
    if len(set(signals[i:i+4])) == 4:
        print(i+4)
        break

for i in range(len(signals)-13):
    if len(set(signals[i:i+14])) == 14:
        print(i+14)
        break