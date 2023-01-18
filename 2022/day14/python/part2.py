cave = open('puzzle_input.txt').read().splitlines()

back = set()
abyss = 0

for line in cave:
    path = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                back.add(x + y * 1j)
                abyss = max(abyss, y + 1)

count = 0

while 500 not in back:
    end = 500
    while True:
        if end.imag >= abyss:
            break
        if end + 1j not in back:
            end += 1j
            continue
        if end + 1j - 1 not in back:
            end += 1j - 1
            continue
        if end + 1j + 1 not in back:
            end += 1j + 1
            continue
        break
    back.add(end)
    count += 1

print(count)