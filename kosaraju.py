# Populate graph and its transposee
v, e = map(int, input().split())
g, gt = [[] for _ in range(v)], [[] for _ in range(v)]
for _ in range(e):
    a, b = map(int, input().split())
    g[a].append(b), gt[b].append(a)

# do DFS toposort
top, vis, scc = [], set(), 0
def DFS(s, add):
    vis.add(s)
    a = gt if add else g
    for v in a[s]:
        if v not in vis: DFS(v, add)
    if add: top.append(s)
for i in range(v):
    if i not in vis: DFS(i, True)

# DFS again on topological order
vis.clear()
for i in top[::-1]:
    if i not in vis: scc += 1; DFS(i, False)