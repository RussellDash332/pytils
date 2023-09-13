from collections import deque
n = 1
g = [[] for _ in range(n)]

# Kahn's algorithm
indeg, top = [0]*n, []
for v in range(n):
    for w in g[v]: indeg[w] += 1
q = deque([i for i in range(n) if indeg[i] == 0])
while q:
    u = q.popleft()
    top.append(u)
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
for i in range(n):
    if i not in vis: DFS(i)
top.reverse()
print(top)