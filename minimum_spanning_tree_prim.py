n = 1
g = [{} for _ in range(n)]
INF = float('inf')

# Prim's algorithm
# Rule of thumb is to run the sparse variant if E < V^1.5
from heapq import *
s = 0 # source node

## sparse variant
mst = [(s, 0)]
pq = [(g[s][t], t) for t in g[s]]; used = [0]*n; used[s] = 1; heapify(pq)
while pq:
    w, u = heappop(pq)
    if used[u]: continue
    mst.append((u, w)); used[u] = 1
    for v in g[u]: heappush(pq, (g[u][v], v))
print(mst)

## dense variant
mst = []; A = [INF]*n; B = [0]*n; A[s] = 0
while len(mst) != n:
    best = (0, A[0])
    for i in range(1, n):
        if A[i] < best[1]: best = (i, A[i])
    mst.append(best)
    A[best[0]], B[best[0]] = INF, 1
    for v in g[best[0]]:
        if not B[v] and A[v] > g[best[0]][v]: A[v] = g[best[0]][v]
print(mst)