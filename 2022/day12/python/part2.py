from collections import deque

mountains = [list(x) for x in open('puzzle_input.txt').read().strip().splitlines()]

for row, i in enumerate(mountains):
    for column, mt in enumerate(i):
        if mt == "S":
            mountains[row][column] = "a"
        if mt == "E":
            end_row = row
            end_column = column
            mountains[row][column] = "z"

path = deque()
path.append((0, end_row, end_column))

back = {(end_row, end_column)}

while path:
    steps, row, column = path.popleft()
    for near_row, near_column in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
        if near_row < 0 or near_column < 0 or near_row >= len(mountains) or near_column >= len(mountains[0]):
            continue
        if (near_row, near_column) in back:
            continue
        if ord(mountains[near_row][near_column]) - ord(mountains[row][column]) < -1:
            continue
        if mountains[near_row][near_column] == "a":
            print(steps + 1)
            exit(0)
        back.add((near_row, near_column))
        path.append((steps + 1, near_row, near_column))