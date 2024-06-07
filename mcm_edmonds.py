# Credits: Brandon Tang
V = 5
g = [[] for _ in range(V)]

# House of Cards, perfect matching of size 5
V = 10; g = [[1, 2], [0, 2, 3, 4], [0, 1, 4, 5], [1, 4, 6, 7], [1, 2, 3, 5, 7, 8], [2, 4, 8, 9], [3, 7], [3, 4, 6, 8], [4, 5, 7, 9], [5, 8]]

# Grid graph, matching of size 4
V = 9; g = [[4, 5, 6], [4, 6, 7], [5, 6, 8], [6, 7, 8], [0, 1], [0, 2], [0, 1, 2, 3], [1, 3], [2, 3]]

def aug(s):
    bs = [*range(V)]; nq = [0]*V; qh = qt = 0; q[0] = s; nq[s] = 1
    while qh <= qt:
        au = q[qh]; qh += 1
        for av in g[au]:
            if bs[au] != bs[av] and mtc[au] != av:
                if av == s or (mtc[av] != -1 and par[mtc[av]] != -1):
                    u, v = au, av; np = [0]*V; nb = [0]*V; uu, vv = u, v
                    while 1:
                        np[(uu:=bs[uu])] = 1
                        if uu == s: break
                        uu = par[mtc[uu]]
                    while 1:
                        if np[(vv:=bs[vv])]: lca = vv; break
                        vv = par[mtc[vv]]
                    for uu in (u, v):
                        while bs[uu] != lca:
                            vv = mtc[uu]; nb[bs[uu]] = nb[bs[vv]] = 1; uu = par[vv]
                            if bs[uu] != lca: par[uu] = vv
                    if bs[u] != lca: par[u] = v
                    if bs[v] != lca: par[v] = u
                    for u in range(V):
                        if nb[bs[u]]:
                            bs[u] = lca
                            if not nq[u]: nq[u] = 1; qt += 1; q[qt] = u
                elif par[av] == -1:
                    par[av] = au
                    if mtc[av] == -1: return av
                    elif not nq[mtc[av]]: nq[mtc[av]] = 1; qt += 1; q[qt] = mtc[av]
    return -1

mcm = 0; mtc = [-1]*V; q = [0]*V
for u in range(V):
    if mtc[u] == -1:
        par = [-1]*V; mcm += (t:=aug(u)) != -1
        while t != -1: v = par[t]; w = mtc[v]; mtc[t], mtc[v] = v, t; t = w
print(mcm)

for i in range(V):
    print(i, 'is matched with', mtc[i])