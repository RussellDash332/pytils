# directed graph taken from https://open.kattis.com/problems/fastestspeedrun
N = 4
G = [{1: 40, 2: 95, 3: 95}, {1: 1, 2: 95, 3: 50}, {1: 20, 2: 95, 3: 1}, {1: 10, 2: 1, 3: 20}]
root = 0
_RECONSTRUCT_TREE = True

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
_BAD = False; H = [-1]*N; Z = 0; S = [-1]*N; S[root] = root; Y = [0]*N
L = []; R = []; D = []; W = []; A = []; B = []
for i in range(N):
    for j in G[i]: W.append(G[i][j]); A.append(i); B.append(j); L.append(-1); R.append(-1); D.append(0); H[j] = merge(H[j], len(W)-1)
if _RECONSTRUCT_TREE: I = [[-1]*2]*N; C = []; P = [-1]*N; U = UFDSRB(N); Q = [None]*N
else: U = UFDS(N)
for s in range(N):
    u = s; q = 0; w = 0
    if _BAD: break
    while S[u] < 0:
        if H[u]<0: print('No such MST'); _BAD = True; break
        e = top(H[u]); Z += e[0]; D[H[u]] -= e[0]; H[u] = pop(H[u]); Y[q] = u
        if _RECONSTRUCT_TREE: Q[q] = e
        q += 1; S[u] = s; u = U.find(e[1])
        if S[u] == s:
            c = -1
            if _RECONSTRUCT_TREE: E = q; T = len(U.o)
            while 1:
                c = merge(c, H[w:=Y[q:=q-1]])
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
    if not _BAD:
        print('MDST length:', Z)
        if _RECONSTRUCT_TREE: print('Parent:', P)