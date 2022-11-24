from collections import deque
import sys
sys.setrecursionlimit(10**5)

g = {}

# Kahn's algorithm
indeg, q = {}, deque([])
for v in g:
    for w in g[v]:
        if w not in indeg: indeg[w] = 0
        indeg[w] += 1
for v in g:
    if v not in indeg:
        q.append(v)
top = []
while q:
    u = q.popleft()
    if u in g:
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0: q.append(v)
print(top)

# DFS toposort
top = []
vis = set()
def DFS(s):
    vis.add(s)
    if s in g:
        for v in g[s]:
            if v not in vis:
                DFS(v) 
    top.append(s)
DFS(0)
top.reverse()
print(top)