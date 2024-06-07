n = 1 # number of vertices
s = 0 # source
INF = float('inf')
D = [INF]*n; p = [-1]*n; D[s] = 0
el = [] # edge list

for _ in range(n-1):
    for a, b, w in el:
        if D[a] != INF and D[b] > D[a]+w: D[b] = D[a]+w; p[b] = a

# Simple negative cycle check
for a, b, w in el:
    if D[a] != INF and D[b] > D[a]+w: assert 0, 'negative cycle detected'

# Thorough negative cycle check, used for kattis/shortestpath3
f = 1; neg = [0]*n
while f:
    f = 0
    for a, b, w in el:
        if D[a] != INF and D[b] > D[a]+w and not neg[b]: D[b] = -INF; neg[b] = 1; f = 1
# neg[i] = 1 implies that i is trapped in a negative cycle
# otherwise, the vertex is still reachable without getting trapped in a negative cycle, assuming D[i] != INF