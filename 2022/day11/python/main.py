input = open("puzzle_input.txt").read().splitlines()

monkeys = []
monkeys_2 = []
operations = []
tests = []
throws_t = []
throws_f = []
W = 1

for a in input:
    if a.startswith('  Starting items'):
        monkeys.append(list(map(int, a.split(': ')[1].split(', '))))
        monkeys_2.append(list(map(int, a.split(': ')[1].split(', '))))
    elif a.startswith('  Operation'):
        operations.append(a.split('= ')[1])
    elif a.startswith('  Test'):
        test = int(a.split('by ')[1])
        W *= test
        tests.append(test)
    elif a.startswith('    If true'):
        throws_t.append(int(a.split('monkey ')[1]))
    elif a.startswith('    If false'):
        throws_f.append(int(a.split('monkey ')[1]))

counts = [0 for _ in monkeys]

for _ in range(20):
    for b in range(len(monkeys)):
        for item in monkeys[b]:
            counts[b] += 1
            old = item
            new = eval(operations[b])
            new //= 3
            if new % tests[b] == 0:
                monkeys[throws_t[b]].append(new)
            else:
                monkeys[throws_f[b]].append(new)
        monkeys[b].clear()
        
counts2 = [0 for _ in monkeys_2]

for _ in range(10000):
    for b in range(len(monkeys_2)):
        for item in monkeys_2[b]:
            counts2[b] += 1
            old = item
            new = eval(operations[b])
            new %= W
            if new % tests[b] == 0:
                monkeys_2[throws_t[b]].append(new)
            else:
                monkeys_2[throws_f[b]].append(new)
        monkeys_2[b].clear()
        
counts.sort()
counts2.sort()
            
print(counts[-1] * counts[-2])
print(counts2[-1] * counts2[-2])