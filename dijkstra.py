from heapq import *

n = 2 # number of vertices
s, t = 0, 1 # source and destination
g = [{} for _ in range(n)]

# Simple version, works like a charm + customizable for state-space Dijkstra
INF = float('inf'); D = [INF]*n; D[s] = 0; pq = [(0, s)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn in g[vv]:
        if D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, (new, nn))
print(D[t])

# Optimized version - coordinate compression + array.array
from array import *
INF = 10**9; D = array('i', [INF]*n); D[s] = 0; pq = [s]
while pq:
    dv = heappop(pq); dd, vv = dv//n, dv%n
    if dd != D[vv]: continue
    for nn in g[vv]:
        if D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, new*n+nn)
print(D[t])