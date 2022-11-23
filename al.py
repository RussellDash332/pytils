import sys

"""
Undirected graph
V, E for vertices and edges
Next E lines specify the edges (u, v, w)
S and T as source and destination

Sample input:

4 3
0 1 3
0 2 1
1 3 4
0 2
"""

g = {}
n, m = map(int, input().split())
for line in sys.stdin:
    m -= 1
    u, v, w = map(int, line.split())
    for _ in range(2):
        if u not in g:      g[u] = {}
        if v not in g[u]:   g[u][v] = w
        g[u][v] = min(g[u][v], w)
        u, v = v, u
    if m == 0: break
s, t = map(int, input().split())