from random import choice

V = 0
g = [[] for _ in range(V)]
free = set()

match = [-1]*V
free2 = set(free)

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1

# regular MCBM
for l in range(V):
    if (can:=[r for r in g[l] if match[r] == -1]): free.discard(l); match[choice(can)] = l
for f in free: vis = [0]*V; aug(f)

# matching graph
mg = [set() for _ in range(V)]
for a in range(V):
    for b in g[a]:
        if match[b] != -1: mg[match[b]].add(b)

# make the graph undirected for DFS prep
el = [(i, j) for i in range(V) for j in g[i]]
for a, b in el: g[b].append(a)

vis, q = [0]*V, []
z = set() # all verts connected to unmatched free verts
for i in free2:
    if not mg[i]: # DFS on unmatched free verts for alternating path
        q.append(2*i)
        while q:
            umt = q.pop()
            u, mt = umt//2, umt%2
            if vis[u]: continue
            z.add(u); vis[u] = 1
            for w in g[u]:
                if (u in mg[w] or w in mg[u])^(1-mt): q.append(2*w+1-mt)

# mvc = (L-Z)|(R&Z)
print([i for i in range(V) if (i in free2)^(i in z)])