g = {}

vis = set()
res = []
def DFS(s):
    stack = [s]
    while stack:
        u = stack.pop()
        vis.add(u)
        res.append(u)
        if u in g:
            for v in g[u]:
                if v not in vis: stack.append(v)