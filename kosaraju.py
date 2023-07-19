# Populate graph and its transpose
v, e = map(int, input().split())
g, gt = [[] for _ in range(v)], [[] for _ in range(v)]
for _ in range(e):
    a, b = map(int, input().split())
    g[a].append(b), gt[b].append(a)

# do DFS toposort
top, vis, scc = [], set(), 0
def DFS(s, t):
    stack = [2*s]; a = g if t else gt
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b and t: top.append(u)
        elif u not in vis:
            vis.add(u)
            stack.append(2*u+1)
            for v in a[u]:
                if v not in vis: stack.append(2*v)
    return 1
for i in range(v):
    if i not in vis: DFS(i, True)

# DFS again on topological order
vis.clear()
for i in top[::-1]:
    if i not in vis: scc += DFS(i, False)