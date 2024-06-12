from collections import deque; INF = float('inf')

def add(u, v, c):
    AL[u].append(len(EL)); EL.append([v, c]); AL[v].append(len(EL)); EL.append([u, 0])

V = 2; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]; mf = 0; p = [-1]*V
while True:
    d = [0]*V; d[source] = 1; q = deque([source])
    while q:
        u = q.popleft()
        if u == sink: break
        for idx in AL[u]:
            v, c = EL[idx]
            if c > 0 and d[v] == 0: d[v] = 1; q.append(v); p[v] = idx
    if not d[sink]: break
    f = INF; s = sink
    while s != source: f = min(f, EL[p[s]][1]); s = EL[p[s]^1][0]
    mf += f; s = sink
    while s != source: EL[p[s]][1] -= f; EL[p[s]^1][1] += f; s = EL[p[s]^1][0]
print(mf)