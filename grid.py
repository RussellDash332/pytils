m = [] # 2D array
R, C = len(m), len(m[0])

# Iterate through elements
for r in range(R):
    for c in range(C):
        pass

# Check neighbours
delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
for dr, dc in delta:
    if 0<=r+dr<R and 0<=c+dc<C:
        pass