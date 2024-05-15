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


# Kruskal's algorithm
class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]
el = []; mst = []; u = UFDS(n)
for a in range(n):
    for b in g[a]: el.append((g[a][b], a, b))
for w, a, b in sorted(el):
    if u.find(a) != u.find(b): u.union(a, b), mst.append((a, b, w))
print(mst)