import sys
sys.setrecursionlimit(10**5)

g = {}

vis = set()
res = []
def DFS(s):
    vis.add(s)
    res.append(s)
    if s in g:
        for v in g[s]:
            if v not in vis:
                DFS(v)