g = {}
v = 1 # number of vertices
INF = float('inf')

def fw(g, v):
    D = [[g[i][j] if i in g and j in g[i] else INF for j in range(v)] for i in range(v)]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    # Negative cycle detection
    for i in range(v):
        for j in range(v):
            for k in range(v):
                if D[i][j] == -INF: break
                if D[i][k] != INF and D[k][j] != INF and D[k][k] < 0:
                    D[i][j] = -INF
    return D

print(fw(g, v))