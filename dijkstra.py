from heapq import *

n = 2 # number of vertices
s, t = 0, 1
INF = float('inf')

g = [{} for _ in range(n)]
D = [INF]*n; D[s] = 0
pq = [(0, s)]
while pq:
    dd, vv = heappop(pq)
    if dd == D[vv]:
        for nn in g[vv]:
            if D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, (new, nn))
print(D[t])