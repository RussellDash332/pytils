from collections import deque, defaultdict
INF = 1e18

def DFS(u, t, f=INF):
    if u == t or f == 0: return f
    vis[u] = 1
    for i in range(last[u], len(AL[u])):
        v, cap, flow, cost = EL[AL[u][i]]
        if not vis[v] and d[v] == d[u]+cost:
            pushed = DFS(v, t, min(f, cap-flow))
            if pushed:
                tc[0] += pushed * cost
                flow += pushed
                EL[AL[u][i]][2] = flow
                EL[AL[u][i]^1][2] -= pushed
                vis[u], last[u] = 0, i
                return pushed
    vis[u] = 0
    return 0

import sys
V, E, s, t = map(int, input().split())
EL, AL, vis, tc = [], [[] for _ in range(V)], [0]*V, [0]
for l in sys.stdin:
    u, v, w, c = map(int, l.split())
    if u != v: EL.append([v, w, 0, c]), AL[u].append(len(EL)-1), EL.append([u, 0, 0, -c]), AL[v].append(len(EL)-1)

mf = 0
d = defaultdict(lambda: INF)
while True:
    d.clear()
    d[s], vis[s] = 0, 1
    q = deque([s])
    while q:
        u = q.popleft()
        vis[u] = 0
        for idx in AL[u]:
            v, cap, flow, cost = EL[idx]
            if cap > flow and d[v] > d[u]+cost:
                d[v] = d[u]+cost
                if not vis[v]: q.append(v); vis[v] = 1
    if d[t] == INF: break
    last = [0]*V
    f = DFS(s, t)
    while f:
        mf += f; f = DFS(s, t)
print(mf, tc[0])