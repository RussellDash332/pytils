n = 1 # number of vertices
g = [[] for _ in range(n)]
uv_pairs = []

# sample tree
n = 5
g = [[1, 2], [0], [0, 3, 4], [2], [2]]
uv_pairs = [[1, 4], [3, 4], [2, 3], [0, 4]]

# Tarjan's OLCA
from array import *
Q = [[] for _ in range(n)]; R = []; d = array('i', [0]*n); par = array('i', range(n)); d[0] = 1; s = [(0, 0)]
for i, (a, b) in enumerate(uv_pairs):
    R.append([a, b, -1]), Q[a].append(i), Q[b].append(i)

def find(i):
    if par[i] == i: return i
    par[i] = find(par[i]); return par[i]

while s:
    ub, p = s.pop(); u = ub//2
    if ub%2:
        for x in Q[u]:
            if R[x][1] == u: R[x][0], R[x][1] = R[x][1], R[x][0]
            R[x][2] = find(R[x][1])
        par[u] = p
    else:
        s.append((ub+1, p))
        for t in g[u]:
            if t != p: d[t] = d[u]+1; s.append((2*t, u))
for a, b, lca in R:
    print(f'LCA of {a} and {b} is {lca}')