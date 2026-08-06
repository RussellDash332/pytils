# Minimum clique cover
# Requires some predefined variables as shown below
# If you don't need to show clique, just remove A and cl
def bt(v, cc):
    global Z, A
    if cc >= Z: return
    if v == n: Z = cc; A = [*cl]; return
    for i in range(1, cc+2):
        if cm[i]&am[v] == cm[i]: cl[v] = i; cm[i] |= 1<<v; bt(v+1, max(cc, i)); cm[i] ^= 1<<v; cl[v] = 0

if __name__ == '__main__':
    G = [
        [1, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    n = len(G); am = [0]*n
    for i in range(n):
        for j in range(n):
            if G[i][j]: am[i] |= 1<<j
    Z, A = n+1, []; cl = [0]*n; cm = [0]*(n+1)
    bt(0, 0)
    print(Z, A) # finalized assignments