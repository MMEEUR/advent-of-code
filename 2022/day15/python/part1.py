import re

splitter = re.compile(r"-?\d+")
Y = 2000000
known = set()
intervals = []

for line in open('puzzle_input.txt').read().splitlines():
    sx, sy, bx, by = map(int, splitter.findall(line))
    
    distinction = abs(sx - bx) + abs(sy - by)
    o = distinction - abs(sy - Y)

    if o < 0:
        continue

    lx = sx - o
    hx = sx + o
    intervals.append((lx, hx))
    
    if by == Y:
        known.add(bx)

intervals.sort()

q = []

for lo, hi in intervals:
    if not q:
        q.append([lo, hi])
        continue

    qlo, qhi = q[-1]

    if lo > qhi + 1:
        q.append([lo, hi])
        continue
    
    q[-1][1] = max(qhi, hi)

cannot = set()

for lo, hi in q:
    for x in range(lo, hi + 1):
        cannot.add(x)

print(len(cannot - known))