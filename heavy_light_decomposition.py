# setup graph and vertex values
# example graph taken from https://cp-algorithms.com/graph/hld.html
from random import *
n = 16
G = [{} for _ in range(n)]
V = [randint(1, 10**2) for _ in range(n)]
E = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (5, 8), (5, 9), (6, 10), (7, 11), (10, 12), (10, 13), (10, 14), (13, 15)]
for a, b in E: G[a][b] = G[b][a] = randint(1, 10**2)

MAXIMIZE = True
USE_EDGE_VALUES = True

obj = [min, max][MAXIMIZE]
DEFAULT_VALUE = [10**18, -10**18][MAXIMIZE]

def pu(i, x):
    i += n; A[i] = x
    while i > 1: i >>= 1; A[i] = min(A[i<<1], A[(i<<1)+1])
def rq(i, j):
    i += n; j += n; x = DEFAULT_VALUE
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = obj(x, A[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = obj(x, A[j-1]); j >>= 1
    return x
def ds(v, p):
    sz[v] = 1; par[v] = p
    for w in G[v]:
        if w != p: dep[w] = dep[p]+1; sz[v] += ds(w, v)
    return sz[v]
def dh(v, p, t, x):
    pos[v] = cur[0]; cur[0] += 1; chn[v] = t; best = hvy = -1; pu(pos[v], x if USE_EDGE_VALUES else V[v])
    for w in G[v]:
        if w != p and sz[w] > best: best = sz[w]; hvy = w
    if hvy == -1: return
    dh(hvy, v, t, G[v][hvy])
    for w in G[v]:
        if p != w != hvy: dh(w, v, w, G[v][w])
def get(x, y):
    xa = []; ya = []; z = DEFAULT_VALUE; ac = -1; ox = x; oy = y
    while x != -1: xa.append(x); x = par[chn[x]]
    while y != -1: ya.append(y); y = par[chn[y]]
    while xa and ya and chn[xa[-1]] == chn[ya[-1]]:
        if pos[xa[-1]] < pos[ya[-1]]: ac = xa[-1]
        else: ac = ya[-1]
        xa.pop(); ya.pop()
    for x in (ox, oy):
        while chn[x] != chn[ac]: z = obj(z, rq(pos[chn[x]], pos[x]+1)); x = par[chn[x]]
        z = obj(z, rq(pos[ac]+USE_EDGE_VALUES, pos[x]+1))
    return z

sz = [0]*n; par = [0]*n; dep = [0]*n; pos = [0]*n; cur = [0]; chn = [0]*n; A = [DEFAULT_VALUE]*2*n; ds(0, -1); dh(0, 0, 0, DEFAULT_VALUE)
for i in range(n):
    for j in range(i):
        print(f'Maximum of {["node", "edge"][USE_EDGE_VALUES]} values along the path between {(i, j)}:', q:=get(i, j))
        assert q == get(j, i)
print('Vertex values:', V)
print('Edge values:', G)