from collections import deque

INF = float('inf')

# from CP4
def BFS(s, t):
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for idx in AL[u]:
            v, cap, flow = EL[idx]
            if cap > flow and d[v] == -1:
                d[v] = d[u]+1
                q.append(v)
                p[v] = (u, idx)
    return d[t] != -1

# from CP4
def DFS(u, t, f=INF):
    if u == t or f == 0: return f
    for i in range(last[u], len(AL[u])):
        last[u] = i
        v, cap, flow = EL[AL[u][i]]
        if d[v] != d[u]+1: continue
        pushed = DFS(v, t, min(f, cap - flow))
        if pushed:
            EL[AL[u][i]][2] += pushed
            EL[AL[u][i]^1][2] -= pushed
            return pushed
    return 0

V, E = 4, 0
directed = True
source, sink = 0, 3
EL, AL = [], [[] for _ in range(V)]
for _ in range(E):
    u, v, capacity = map(int, input().split())
    EL.append([v, capacity, 0]), AL[u].append(len(EL)-1), EL.append([u, 0 if directed else capacity, 0]), AL[v].append(len(EL)-1)

# Dinic's algorithm, to be run only once
mf = 0
p, d = [(-1, -1) for _ in range(V)], [-1]*V
while BFS(source, sink):
    last = [0]*V
    f = DFS(source, sink)
    while f: mf += f; f = DFS(source, sink)
    p, d = [(-1, -1) for _ in range(V)], [-1]*V
print(mf)