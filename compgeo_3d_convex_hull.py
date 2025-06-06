# Represent a point as a tuple (x, y, z) and a polyhedron as a list of points
# 3D convex hull is represented as a list of triangles (3D point triplets)
def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def cross_util(a, b):
    return a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]
def cross(a, b, c):
    return cross_util((b[0]-a[0], b[1]-a[1], b[2]-a[2]), (c[0]-a[0], c[1]-a[1], c[2]-a[2]))

# O(n^2) KACTL, no four points are coplanar
def chull_old(A):
    F = []; n = len(A); K = ((1, 2), (1, 3), (2, 3))
    E = [[[] for _ in range(n)] for _ in range(n)]
    def mf(i, j, k, l):
        q = cross(A[i], A[j], A[k])
        if dot(q, A[l]) > dot(q, A[i]): q = (-q[0], -q[1], -q[2])
        E[i][j].append(k); E[i][k].append(j); E[j][k].append(i); F.append([q, i, j, k])
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4): mf(i, j, k, 6-i-j-k)
    for i in range(4, n):
        j = 0
        while j < len(F):
            f = F[j]
            if dot(f[0], A[i]) > dot(f[0], A[f[1]]):
                for a, b in K: E[f[a]][f[b]].remove(f[6-a-b])
                F[j], F[-1] = F[-1], F[j]; F.pop(); j -= 1
            j += 1
        for j in range(len(F)):
            f = F[j]
            for a, b in K:
                if len(E[f[a]][f[b]]) != 2: mf(f[a], f[b], i, f[6-a-b])
    for f in F:
        if dot(cross(A[f[1]], A[f[2]], A[f[3]]), f[0]) <= 0: f[2], f[3] = f[3], f[2]
    return [(A[f[1]], A[f[2]], A[f[3]]) for f in F]

# Credits to Jeremy Lim
# https://algolist.ru/maths/geom/convhull/qhull3d.html
# Runs in expected O(N log N) time, supposedly faster than the Clarkson-Shor randomized incremental algorithm (by a constant factor?)
from random import *
def vol(a, b, c, d):
    return dot(cross(a, b, c), (d[0]-a[0], d[1]-a[1], d[2]-a[2]))
def col(a, b, c):
    return a == b or a == c or b == c or cross(a, b, c) == (0, 0, 0)
def chull(P, K=100):
    P = sorted({*P}) # adjust accordingly
    N = len(P); V = []; T = []; S = []; I = []; Ln = []; Lh = []; C = []; B = []; U = [0]*N; D = [1, 0, 2, 0, 3, 0, 2, 1, 3, 1, 3, 2]; F = [-1]*12
    def af(p, q, r): l = len(C); C.append((p, q, r)); V.append(l); F[p] = F[q] = F[r] = l; T.append(l); Lh.append(-1); S.append(0); I.append(False)
    def fvp(f, d): a, b, c = fv(f); return vol(P[a], P[b], P[c], P[d]) > 0
    def fv(f): p, q, r = C[f]; return D[p], D[q], D[r]
    for i in range(2, N):
        if not col(P[0], P[1], P[i]): P[i], P[2] = P[2], P[i]; break
    for i in range(i+1, N):
        if vol(P[0], P[1], P[2], P[i]): P[i], P[3] = P[3], P[i]; break
    if vol(P[0], P[1], P[2], P[3]) < 0: P[1], P[2] = P[2], P[1]
    af(7, 1, 2); af(5, 0, 8); af(9, 6, 10); af(11, 3, 4)
    for i in range(4, N):
        for f in V:
            if fvp(f, i): Ln.append(Lh[f]); Lh[f] = len(B); B.append(i); break
    while T:
        if S[v:=T.pop()] == 1 or Lh[v] == -1: continue
        a, b, c = fv(v); S[v] = 1; M = -10**18; x = -1; i = Lh[v]; Vs = [v]; Ns = []; H = []; Q = 0
        while i != -1:
            w = vol(P[a], P[b], P[c], P[B[i]])
            if M < w: M = w; x = B[i]
            i = Ln[i]
        for f in Vs:
            for e in C[f]:
                if S[g:=F[e^1]] < 1:
                    if fvp(g, x): S[g] = 1; Vs.append(g)
                    else: S[g] = 2; Ns.append(g)
                if S[g] == 2: U[D[e]] = len(D); D.append(x); F.append(-1); D.append(D[e]); F.append(-1); H.append(e)
        for e in H: af(U[D[e]], U[D[e^1]]^1, e)
        for f in Vs:
            i = Lh[f]
            while i != -1:
                if B[i] != x:
                    if (Q:=Q+1) == K: shuffle(H); Q = 0
                    for e in H:
                        if fvp(F[e], B[i]): Ln.append(Lh[F[e]]); Lh[F[e]] = len(B); B.append(B[i]); break
                i = Ln[i]
        for f in Vs: I[f] = True; Lh[f] = -1
        for f in Ns: S[f] = 0
    return [[P[j] for j in fv(i)] for i in V if not I[i]]

if __name__ == '__main__':
    from time import *

    P = [(1, 0, 0), (1, 1, 0), (0, 0, 0), (0, 0, 1)]
    print(C:=chull(P))
    assert sorted(map(sorted, C)) == sorted(map(sorted, chull_old(P)))
    print('Old and new 3D convex hulls are the same')

    P = [(0, 0, 0), (100, 0, 0), (0, 100, 0), (0, 0, 100), (20, 20, 20), (30, 20, 10)]
    print(C:=chull(P))
    assert sorted(map(sorted, C)) == sorted(map(sorted, chull_old(P)))
    print('Old and new 3D convex hulls are the same')

    # random but small, hopefully no 4 points are coplanar
    seed(42)
    L = 10**5; R = randint(2*L*L, L**3); N = randint(10**3, 10**4)
    P = [(x:=randint(-L, L), y:=randint(-L, L), choice([-1, 1])*int((R-x*x-y*y)**.5)) for _ in range(N)]
    T = time()
    print('[old] 3D convex hull has', len(D:=chull_old(P)), f'faces (N={N}), takes', round(time()-T, 3), 'seconds')
    T = time()
    print('[new] 3D convex hull has', len(C:=chull(P)), f'faces (N={N}), takes', round(time()-T, 3), 'seconds')
    assert sorted(map(sorted, C)) == sorted(map(sorted, D))
    print('Old and new 3D convex hulls are the same')

    # big near-sphere, old O(n^2) should be slow at this point
    L = 10**5; R = randint(2*L*L, L**3); N = randint(3*10**4, 5*10**4)
    P = [(x:=randint(-L, L), y:=randint(-L, L), choice([-1, 1])*int((R-x*x-y*y)**.5)) for _ in range(N)]
    T = time()
    print('[new] 3D convex hull has', len(chull(P)), f'faces (N={N}), takes', round(time()-T, 3), 'seconds')

    # another big near-sphere, old O(n^2) should be slow at this point
    L = 10**5; R = randint(2*L*L, L**3); N = randint(5*10**4, 10**5)
    P = [(x:=randint(-L, L), y:=randint(-L, L), choice([-1, 1])*int((R-x*x-y*y)**.5)) for _ in range(N)]
    for i in range(N): P[i] = list(P[i]); shuffle(P[i]); P[i] = tuple(P[i])
    T = time()
    print('[new] 3D convex hull has', len(chull(P)), f'faces (N={N}), takes', round(time()-T, 3), 'seconds')