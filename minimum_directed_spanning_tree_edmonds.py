class UFDS:
    def __init__(s, N): s.p = [*range(N)]; s.r = [0]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i]); return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]
            return 1 # need to return a truthy

class UFDSC:
    def __init__(s, N): s.p = [*range(N)]; s.r = [-1]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i]); return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)): s.p[y] = s.r[y] = x

class UFDSRB:
    def __init__(s, n): s.p = [-1]*n; s.o = []
    def find(s, u):
        while s.p[u] > -1: u = s.p[u]
        return u
    def union(s, u, v):
        if (u:=s.find(u)) != (v:=s.find(v)):
            if s.p[u] > s.p[v]: u, v = v, u
            s.o.append((v, s.p[v])); s.p[u] += s.p[v]; s.p[v] = u
            return 1 # need to return a truthy
    def undo(s):
        if s.o: v, x = s.o.pop(); s.p[s.p[v]] -= x; s.p[v] = x

# G is an adjacency list
def edmonds_sparse(G, root, reconstruct_tree=True):
    def prop(s):
        if ~L[s]: D[L[s]] += D[s]
        if ~R[s]: D[R[s]] += D[s]
        W[s] += D[s]; D[s] = 0
    def merge(a, b):
        S = [(a, b, 0)]; T = []
        while S:
            a, b, p = S.pop()
            if p: L[a], R[a] = T.pop(), L[a]; T.append(a)
            else:
                if a<0 or b<0: T.append(a if ~a else b)
                else:
                    prop(a); prop(b)
                    if W[a] > W[b]: a, b = b, a
                    S.append((a, b, 1)); S.append((b, R[a], 0))
        return T.pop()
    def top(s): prop(s); return (W[s], A[s], B[s])
    def pop(a): prop(a); return merge(L[a], R[a])
    H = [-1]*N; Z = 0; S = [-1]*N; S[root] = root; Y = [0]*N
    L = []; R = []; D = []; W = []; A = []; B = []
    for i in range(N):
        for j in G[i]: W.append(G[i][j]); A.append(i); B.append(j); L.append(-1); R.append(-1); D.append(0); H[j] = merge(H[j], len(W)-1)
    if reconstruct_tree: I = [[-1]*2]*N; C = []; P = [-1]*N; U = UFDSRB(N); Q = [None]*N
    else: U = UFDS(N)
    for s in range(N):
        u = s; q = 0; w = 0
        while S[u] < 0:
            if H[u]<0: return None, None
            e = top(H[u]); Z += e[0]; D[H[u]] -= e[0]; H[u] = pop(H[u]); Y[q] = u
            if reconstruct_tree: Q[q] = e
            q += 1; S[u] = s; u = U.find(e[1])
            if S[u] == s:
                c = -1
                if reconstruct_tree: E = q; T = len(U.o)
                while 1:
                    c = merge(c, H[w:=Y[q:=q-1]])
                    if not U.union(u, w): break
                H[u:=U.find(u)] = c; S[u] = -1
                if reconstruct_tree: C.append((u, T, Q[q:E]))
        if reconstruct_tree:
            for i in range(q): I[U.find(Q[i][2])] = Q[i]
    if reconstruct_tree:
        while C:
            u, t, v = C.pop(); f = I[u]
            while len(U.o) > t: U.undo()
            for e in v: I[U.find(e[2])] = e
            I[U.find(f[2])] = f
        for i in range(N):
            if I[i]: P[i] = I[i][1]
    return (Z, P if reconstruct_tree else None)

# G is an adjacency list
# Credits to Jeremy Lim for the idea
def edmonds_dense(G, root, reconstruct_tree=True):
    INF = 10**18
    T = [sorted((-G[i][j], i) for i in range(N) if j in G[i]) for j in range(N)] # transpose and sort
    W = [0]*N; L = [0]*N; C = [None]*N; Z = 0
    if reconstruct_tree: U = UFDSC(N); H = []
    else: U = UFDS(N)
    while 1:
        r = U.find(root)
        for v in range(N):
            if v == U.find(v): W[v] = INF if v != r else 0; C[v] = None
        for v in range(N):
            while T[v] and U.find(v) == U.find(T[v][-1][1]): T[v].pop()
            if T[v]:
                w, u = T[v][-1]; c = -w-L[v]; x = U.find(v)
                if W[x] > c: W[x] = c; C[x] = (u, v)
        for v in range(N):
            if v == U.find(v) and W[v] >= INF: return None, None
        D = []; S = [0]*N; S[r] = 1; q = 2; Y = [0]*N
        for v in range(N):
            if v == U.find(v) and not S[v]:
                u = v; s = []
                while not S[u]: S[u] = q; s.append(u); u = U.find(C[u][0])
                if S[u] == q:
                    Y[u] = 1; c = [u]
                    while s[-1] != u: Y[s[-1]] = 1; c.append(s.pop())
                    D.append(c)
                q += 1
        if D:
            for v in range(N):
                if Y[x:=U.find(v)]:
                    if v == x: Z += W[v]
                    L[v] += W[x]
            for k in D:
                for c in k: U.union(k[0], c)
                if reconstruct_tree:
                    e = []
                    for c in k: e.append(C[c])
                    H.append((k, e))
            continue
        for v in range(N):
            if v == U.find(v): Z += W[v]
        break
    if not reconstruct_tree: return Z, None
    P = [-1]*N
    for v in range(N):
        if v == U.find(v):
            if v == U.find(root): C[v] = (-1, root)
            else: P[C[v][1]] = C[v][0]
    while H:
        K, E = H.pop(); u, v = C[K[0]]; t = v
        for k in K: S[k] = q
        while t != -1 and S[t] != q: t = U.r[t]
        q += 1
        for k, (x, y) in zip(K, E):
            if k == t: P[v] = u; C[k] = (u, v)
            else: P[y] = x; C[k] = (x, y)
    return Z, P

if __name__ == '__main__':
    from random import *
    from time import *
    def create_sparse_graph(N, M):
        U = UFDS(N); C = N; G = [{} for _ in range(N)]
        while C > 1:
            a, b = sample(range(N), 2)
            if U.find(a) != U.find(b): C -= 1; U.union(a, b); G[a][b] = randint(1, 10**9); G[b][a] = randint(1, 10**9); M -= 1
        while M:
            a, b = sample(range(N), 2)
            if b not in G[a]: G[a][b] = randint(1, 10**9); G[b][a] = randint(1, 10**9); M -= 1
        return G, randint(0, N-1)
    def create_dense_graph(N):
        G = [{} for _ in range(N)]
        for a in range(N):
            for b in range(a): G[a][b] = randint(1, 10**9); G[b][a] = randint(1, 10**9)
        return G, randint(0, N-1)
    def create_forest_graph(N):
        G = [{} for _ in range(N)]
        k = randint(2, N//2)
        for i in range(N//k+1):
            for a in range(k*i, min(k*i+k, N)):
                for b in range(k*i, a): G[a][b] = randint(1, 10**9); G[b][a] = randint(1, 10**9)
        return G, randint(0, N-1)

    # directed graph taken from https://open.kattis.com/problems/fastestspeedrun
    N = 4
    G = [{1: 40, 2: 95, 3: 95}, {1: 1, 2: 95, 3: 50}, {1: 20, 2: 95, 3: 1}, {1: 10, 2: 1, 3: 20}]
    print('MDST with sparse Edmonds:', edmonds_sparse(G, 0), edmonds_sparse(G, 0, 0))
    print('MDST with dense Edmonds: ', edmonds_dense(G, 0), edmonds_dense(G, 0, 0))

    # random small sparse graph
    N = randint(20, 100)
    M = randint(N-1, 2*N+67)
    print('\nRandom graph with', N, 'vertices and', M, 'edges')
    G, root = create_sparse_graph(N, M)
    print('MDST length with sparse Edmonds:', x1:=edmonds_sparse(G, root, 0)[0])
    print('MDST length with dense Edmonds: ', x2:=edmonds_dense(G, root, 0)[0])
    z1, p1 = edmonds_sparse(G, root)
    z2, p2 = edmonds_dense(G, root)
    assert p1 == p2
    assert x1 == x2 == z1 == z2, ((z1, z2), (x1, x2))

    # random disconnected graph
    N = randint(20, 100)
    print('\nDisconnected graph with', N, 'vertices')
    G, root = create_forest_graph(N)
    print('MDST length with sparse Edmonds:', x1:=edmonds_sparse(G, root, 0)[0])
    print('MDST length with dense Edmonds: ', x2:=edmonds_dense(G, root, 0)[0])
    z1, p1 = edmonds_sparse(G, root)
    z2, p2 = edmonds_dense(G, root)
    assert p1 == p2
    assert x1 == x2 == z1 == z2, ((z1, z2), (x1, x2))

    # random small complete graph
    N = randint(100, 300)
    print('\nRandom **complete** graph with', N, 'vertices')
    G, root = create_dense_graph(N)
    for rc in range(2):
        print('Reconstruct tree?', bool(rc))
        T = time(); z1, p1 = edmonds_sparse(G, root, rc); T_CLE = time()-T
        print('    Time elapsed for sparse Edmonds:', round(T_CLE, 5))
        T = time(); z2, p2 = edmonds_dense(G, root, rc); T_ED = time()-T
        print('    Time elapsed for dense Edmonds: ', round(T_ED, 5))
        assert z1 == z2 and p1 == p2

    # random medium sparse graph
    N = randint(1000, 2500)
    M = randint(N, 10000)
    print('\nRandom graph with', N, 'vertices and', M, 'edges')
    G, root = create_sparse_graph(N, M)
    for rc in range(2):
        print('Reconstruct tree?', bool(rc))
        T = time(); z1, p1 = edmonds_sparse(G, root, rc); T_CLE = time()-T
        print('    Time elapsed for sparse Edmonds:', round(T_CLE, 5))
        T = time(); z2, p2 = edmonds_dense(G, root, rc); T_ED = time()-T
        print('    Time elapsed for dense Edmonds: ', round(T_ED, 5))
        assert z1 == z2 and p1 == p2

    # random medium complete graph
    N = randint(1000, 2500)
    print('\nRandom **complete** graph with', N, 'vertices')
    G, root = create_dense_graph(N)
    for rc in range(2):
        print('Reconstruct tree?', bool(rc))
        T = time(); z1, p1 = edmonds_sparse(G, root, rc); T_CLE = time()-T
        print('    Time elapsed for sparse Edmonds:', round(T_CLE, 5))
        T = time(); z2, p2 = edmonds_dense(G, root, rc); T_ED = time()-T
        print('    Time elapsed for dense Edmonds: ', round(T_ED, 5))
        assert z1 == z2 and p1 == p2

    # random large sparse graph
    N = randint(50000, 200000)
    M = randint(N, 200000)
    print('\nRandom graph with', N, 'vertices and', M, 'edges')
    G, root = create_sparse_graph(N, M)
    print('MDST length with sparse Edmonds:', edmonds_sparse(G, root, 0)[0])
    #print('MDST length with dense Edmonds: ', edmonds_dense(G, root, 0)[0])