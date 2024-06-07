from collections import deque

n = 1 # number of vertices
s = 0 # source vertex
g = [[] for _ in range(n)]

q = deque([s]); vis = [0]*n; res = []
while q:
    u = q.popleft()
    if vis[u]: continue
    vis[u] = 1; res.append(u)
    for v in g[u]: q.append(v)

print(res) # traversal result