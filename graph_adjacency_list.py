import sys; input = sys.stdin.readline

"""
(Un)directed graph (customizable)
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

n, m = map(int, input().split())
g = [{} for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    for _ in range(2):
        if v not in g[u]: g[u][v] = w
        g[u][v] = min(g[u][v], w)
        u, v = v, u
s, t = map(int, input().split())


"""
Unweighted version

Sample input:
4 3
0 1
0 2
1 3
0 2
"""

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m): u, v, w = map(int, input().split()); g[u].append(v), g[v].append(u)
s, t = map(int, input().split())