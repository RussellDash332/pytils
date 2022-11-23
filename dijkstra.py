from heapq import *

g = {}
s, t = 0, 1

def dijkstra(D, s):
    D[s] = 0
    pq = [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd == D[vv] and vv in g:
            for nn in g[vv]:
                if nn not in D or D[nn] > dd + g[vv][nn]:
                    D[nn] = dd + g[vv][nn]
                    heappush(pq, (D[nn], nn))

D = {}
dijkstra(D, s)
if t not in D:  print(-1)
else:           print(D[t])