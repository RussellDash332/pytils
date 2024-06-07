import sys

# Constants
ACTIVE_CHAR = '#'
INACTIVE_CHAR = '.'
ACTIVE_NB = [2, 3]  # active cells with this many neighbour(s) remain active
INACTIVE_NB = [3]   # inactive cells with this many neighbour(s) becomes active
TIME = 6

def num_active(x, y):
    ans = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            ans += d.get((x + dx, y + dy), 0)
    return ans - d.get((x, y), 0)

def draw(d):
    g = [[(INACTIVE_CHAR + ACTIVE_CHAR)[d.get((i, j), 0)] for j in range(len(m[0]))] for i in range(len(m))]
    for r in g:
        print(''.join(r))

"""

.........
.........
....#....
...###...
...#.#...
....#....
.........
.........

"""

m = []
for line in sys.stdin:
    m.append(list(line.strip()))

d = {}
for i in range(len(m)):
    for j in range(len(m[0])):
        d[(i, j)] = int(m[i][j] == ACTIVE_CHAR)

def tick(d):
    new_d = {}
    for x, y in d:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if d.get((x + dx, y + dy), 0):
                    new_d[(x + dx, y + dy)] = int(num_active(x + dx, y + dy) in ACTIVE_NB)
                else:
                    new_d[(x + dx, y + dy)] = int(num_active(x + dx, y + dy) in INACTIVE_NB)
    return new_d

for t in range(TIME):
    d = tick(d)
    print('Generation', t+1)
    draw(d)
    print()