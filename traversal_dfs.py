n = 1 # number of vertices
s = 0 # source vertex
g = [[] for _ in range(n)]

# pre-processing
vis = [0]*n; res = []
stack = [s]
while stack:
    u = stack.pop()
    if vis[u]: continue
    vis[u] = 1; res.append(u)
    for v in g[u]: stack.append(v)

# post-processing
vis = [0]*n; res = []
stack = [2*s]
while stack:
    ub = stack.pop()
    u, b = ub//2, ub%2
    if b: res.append(u)
    elif not vis[u]:
        vis[u] = 1; stack.append(2*u+1)
        for v in g[u]: stack.append(2*v)