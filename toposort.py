from collections import deque
g = {}

# Kahn's algorithm
indeg, q, top = {}, deque(), []
for v in g:
    for w in g[v]:
        if w not in indeg: indeg[w] = 0
        indeg[w] += 1
for v in g:
    if v not in indeg:
        q.append(v)
while q:
    u = q.popleft()
    top.append(u)
    if u in g:
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0: q.append(v)
print(top)

# DFS toposort
top, vis = [], set()
def DFS(s):
    stack = [2*s]
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b: top.append(u)
        elif u not in vis:
            vis.add(u)
            stack.append(2*u+1)
            for v in g[u]:
                if v not in vis: stack.append(2*v)
for i in g:
    if i not in vis: DFS(i)
top.reverse()
print(top)