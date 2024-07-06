# Minimum path cover in a DAG
# G is the original graph, g is the transformed graph
from random import *

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

V = 5
G = [[] for _ in range(V)]
g = [[] for _ in range(2*V)]
for i in range(V):
    for j in G[i]: g[i].append(j+V)
match, mcbm = [-1]*2*V, 0
free = {*range(V)}; nfree = len(free)
for l in [*free]:
    if (candidates:=[r for r in g[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
for f in free: vis = [0]*nfree; mcbm += aug(f)
print(V-mcbm)