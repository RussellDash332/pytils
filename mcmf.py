from collections import deque, defaultdict
import sys
INF = 1e18

def mcmf1():
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

def mcmf2():
    n, m, s, t = map(int, input().split())
    al, el, k = [[] for _ in range(n)], [], INF
    for l in sys.stdin:
        u, v, c, w = map(int, l.split())
        e1, e2 = [u, v, c, w, 0, len(al[v])], [v, u, 0, -w, 0, len(al[u])]
        al[u].append(len(el)), el.append(e1), al[v].append(len(el)), el.append(e2)
    flow = cost = 0
    while flow < k:
        id, d, q, p, pe = [0]*n, [INF]*n, [0]*n, [0]*n, [0]*n
        qh = qt = 0
        q[qt] = s; qt += 1
        d[s] = 0
        while qh != qt:
            v = q[qh]; qh += 1
            id[v] = 2
            if qh == n: qh = 0
            for i in range(len(al[v])):
                r = el[al[v][i]]
                if r[4] < r[2] and d[v]+r[3] < d[r[1]]:
                    d[r[1]] = d[v]+r[3]
                    if id[r[1]] == 0:
                        q[qt] = r[1]; qt += 1
                        if qt == n: qt = 0
                    elif id[r[1]] == 2:
                        qh -= 1
                        if qh == -1: qh = n-1
                        q[qh] = r[1]
                    id[r[1]] = 1; p[r[1]] = v; pe[r[1]] = i
        if d[t] == INF: break
        addflow, v = k-flow, t
        while v != s:
            ee = al[p[v]][pe[v]]
            addflow = min(addflow, el[ee][2]-el[ee][4])
            v = p[v]
        v = t
        while v != s:
            ee = al[p[v]][pe[v]]
            el[ee][4] += addflow
            el[al[v][el[ee][5]]][4] -= addflow
            cost += el[ee][3]*addflow
            v = p[v]
        flow += addflow
    print(flow, cost)

if __name__ == '__main__':
    #mcmf1()
    mcmf2()