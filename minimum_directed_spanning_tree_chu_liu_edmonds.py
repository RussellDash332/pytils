# directed graph taken from https://open.kattis.com/problems/fastestspeedrun
N = 4
G = [{1: 40, 2: 95, 3: 95}, {1: 1, 2: 95, 3: 50}, {1: 20, 2: 95, 3: 1}, {1: 10, 2: 1, 3: 20}]
root = 0
_RECONSTRUCT_TREE = True
_BAD = False

class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]
            return 1
class UFDSRB:
    def __init__(s, n):
        s.p = [-1]*n; s.o = []
    def find(s, u):
        while s.p[u] > -1: u = s.p[u]
        return u
    def union(s, u, v):
        if (u:=s.find(u)) != (v:=s.find(v)):
            if s.p[u] > s.p[v]: u, v = v, u
            s.o.append((v, s.p[v])); s.p[u] += s.p[v]; s.p[v] = u
            return 1
    def undo(s):
        if s.o: v, x = s.o.pop(); s.p[s.p[v]] -= x; s.p[v] = x
class Node:
    def __init__(s, k):
        s.k = k; s.l = s.r = None; s.d = 0
    def prop(s):
        s.k[0] += s.d
        if s.l: s.l.d += s.d
        if s.r: s.r.d += s.d
        s.d = 0
    def top(s):
        s.prop(); return s.k
def merge(a, b):
    if not a or not b: return a or b
    a.prop(); b.prop()
    if a.k[0] > b.k[0]: a, b = b, a
    a.l, a.r = merge(b, a.r), a.l; return a
def pop(a): a.prop(); return merge(a.l, a.r)
E = []; H = [None]*N; Z = 0; S = [-1]*N; S[root] = root; R = [0]*N; Q = [None]*N
for i in range(N):
    for j in G[i]: E.append((G[i][j], i, j))
for w, a, b in E: H[b] = merge(H[b], Node([w, a, b]))
if _RECONSTRUCT_TREE: I = [[-1]*2]*N; C = []; P = [-1]*N; U = UFDSRB(N)
else: U = UFDS(N)
for s in range(N):
    u = s; q = 0; w = 0
    if _BAD: break
    while S[u] < 0:
        if not H[u]: print('No such MST'); _BAD = True; break
        e = H[u].top(); Z += e[0]; H[u].d -= e[0]; H[u] = pop(H[u]); Q[q] = e; R[q] = u; q += 1; S[u] = s; u = U.find(e[1])
        if S[u] == s:
            c = None; E = q
            if _RECONSTRUCT_TREE: T = len(U.o)
            while 1:
                c = merge(c, H[w:=R[q:=q-1]])
                if not U.union(u, w): break
            H[u:=U.find(u)] = c; S[u] = -1
            if _RECONSTRUCT_TREE: C.append((u, T, Q[q:E]))
    if _RECONSTRUCT_TREE:
        for i in range(q): I[U.find(Q[i][2])] = Q[i]
if _RECONSTRUCT_TREE and not _BAD:
    while C:
        u, t, v = C.pop(); f = I[u]
        while len(U.o) > t: U.undo()
        for e in v: I[U.find(e[2])] = e
        I[U.find(f[2])] = f
    for i in range(N):
        if I[i]: P[i] = I[i][1]

if __name__ == '__main__':
    print('MDST length:', Z)
    if _RECONSTRUCT_TREE: print('Parent:', P)