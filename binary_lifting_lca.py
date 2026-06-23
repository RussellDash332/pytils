N = 10
G = [[] for _ in range(N)]
root = 0

G = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1, 7], [2, 8], [2, 9], [4], [5], [6]]
N = len(G)
root = 0

# jmp[v][k] = vertex reached after going up 2**k steps from v
tin = [0]*N
tout = [0]*N
L = (N-1).bit_length()+1
jmp = [[-1]*L for _ in range(N)]

# preprocess with DFS
stk = [(0, 0, T:=0)]
while stk:
    u, p, b = stk.pop()
    if b: tout[u] = (T:=T+1)
    else:
        tin[u] = (T:=T+1); stk.append((u, p, 1)); jmp[u][0] = p
        for i in range(1, L): jmp[u][i] = jmp[jmp[u][i-1]][i-1]
        for v in G[u]:
            if v != p: stk.append((v, u, 0))

def lca(a, b):
    if tin[a] <= tin[b] < tout[b] <= tout[a]: return a
    if tin[b] <= tin[a] < tout[a] <= tout[b]: return b
    for i in range(L-1, -1, -1):
        j = jmp[a][i]
        if tin[j] > tin[b] or tout[b] > tout[j]: a = j
    return jmp[a][0]

"""
          0
        /   \
       1     2
      / \   / \
     3   4 5   6
        /   \   \
       7     8   9
"""

for u in range(N):
    for v in range(u+1, N):
        print(f'LCA of {u} and {v} is {lca(u, v)}')
        assert lca(u, v) == lca(v, u)