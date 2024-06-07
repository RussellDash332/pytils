v = 1 # number of vertices
INF = float('inf')

# Regular variant - basic form
g = [{} for _ in range(v)]
D = [[g[i][j] if j in g[i] else INF for j in range(v)] for i in range(v)]
for k in range(v):
    for i in range(v):
        for j in range(v): D[i][j] = min(D[i][j], D[i][k] + D[k][j])

# Transitive closure - reachability
g = [set() for _ in range(v)]
D = [[int(j in g[i]) for j in range(v)] for i in range(v)]
for k in range(v):
    for i in range(v):
        for j in range(v): D[i][j] |= D[i][k]&D[k][j]

# Minimax - for MST
g = [{} for _ in range(v)]
D = [[g[i][j] if j in g[i] else INF for j in range(v)] for i in range(v)]
for k in range(v):
    for i in range(v):
        for j in range(v): D[i][j] = min(D[i][j], max(D[i][k], D[k][j]))

# Maximin - for MaxST
g = [{} for _ in range(v)]
D = [[g[i][j] if j in g[i] else INF for j in range(v)] for i in range(v)]
for k in range(v):
    for i in range(v):
        for j in range(v): D[i][j] = max(D[i][j], min(D[i][k], D[k][j]))

# Negative cycle detection - version 1
g = [{} for _ in range(v)]
D = [[g[i][j] if j in g[i] else INF for j in range(v)] for i in range(v)]
for k in range(v):
    for i in range(v):
        for j in range(v): D[i][j] = min(D[i][j], D[i][k] + D[k][j])
for i in range(v):
    for j in range(v):
        for k in range(v):
            if D[i][j] == -INF: break
            if D[i][k] != INF and D[k][j] != INF and D[k][k] < 0: D[i][j] = -INF

# Negative cycle detection - version 2
g = [{} for _ in range(v)]
D = [[g[i][j] if j in g[i] else INF for j in range(v)] for i in range(v)]
for i in range(v): D[i][i] = INF
for k in range(v):
    for i in range(v):
        for j in range(v): D[i][j] = min(D[i][j], D[i][k] + D[k][j])
cyc = [i for i in range(v) if D[i][i]<0]

# Positive cycle detection
g = [{} for _ in range(v)]
D = [[g[i][j] if j in g[i] else INF for j in range(v)] for i in range(v)]
for i in range(v): D[i][i] = INF
for k in range(v):
    for i in range(v):
        for j in range(v): D[i][j] = min(D[i][j], D[i][k] + D[k][j])
cyc = [i for i in range(v) if 0<=D[i][i]<INF]

# Print path
g = [{} for _ in range(v)]
D = [[g[i][j] if j in g[i] else INF for j in range(v)] for i in range(v)]
p = [[i for _ in range(v)] for i in range(v)]
for k in range(v):
    for i in range(v):
        for j in range(v):
            if D[i][j]>(new:=D[i][k]+D[k][j]): D[i][j], p[i][j] = new, p[k][j]