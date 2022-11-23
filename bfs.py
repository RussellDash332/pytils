from collections import deque

g = {}

def bfs(s):
    q = deque([s])
    vis = set()
    res = []
    while q:
        u = q.popleft()
        if u in vis: continue
        vis.add(u)
        res.append(u)
        if u in g:
            for v in g[u]:
                q.append(v)
    return res