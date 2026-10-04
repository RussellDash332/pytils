# Tested in https://open.kattis.com/problems/umferdarljos
G = [
    (-3, 1, 5, -3),
    (5, 4, 2, -4),
    (-1, -1, 7, 3),
    (2, 3, 5, -6),
    (-3, 0, 10, 1)
]
N = len(G)

# Multiple segments intersecting in one point
G = [(-5, -5, 5, 5), (-5, 5, 5, -5), (-10, 0, 10, 0), (0, -10, 0, 10), (-1, -100, -1, 100)]
N = len(G)

from heapq import *; from random import *; from array import *; from math import *
V = array('i'); L = array('i'); R = array('i'); O = array('I'); C = array('I')
P = array('i'); M = {}
class QK:
    def __init__(s, v, u, d=1):
        if d < 0: v = -v; u = -u; d = -d
        s.v = v; s.u = u; s.d = d
    def __lt__(s, o):
        q = s.v*o.d-o.v*s.d
        if q: return q < 0
        return s.u*o.d < o.u*s.d
    def __eq__(s, o):
        return s.v*o.d == o.v*s.d and s.u*o.d == o.u*s.d
def node(v):
    i = len(V); V.append(v); L.append(-1); R.append(-1); P.append(-1); O.append(randint(1, 10**9)); C.append(1); M.setdefault(v, []).append(i); return i
def cnt(x):
    return C[x] if ~x else 0
def pull(x):
    if ~x:
        C[x] = 1+cnt(L[x])+cnt(R[x])
        if ~L[x]: P[L[x]] = x
        if ~R[x]: P[R[x]] = x
def merge(a, b):
    if a < 0 or b < 0:
        z = a if b < 0 else b
        if ~z: P[z] = -1
        return z
    if O[a] < O[b]: R[a] = merge(R[a], b); pull(a); P[a] = -1; return a
    else: L[b] = merge(a, L[b]); pull(b); P[b] = -1; return b
def split(t, k):
    if t < 0: return -1, -1
    if k <= (z:=cnt(L[t])):
        a, b = split(L[t], k); L[t] = b; pull(t); P[t] = -1
        if ~a: P[a] = -1
        return a, t
    else:
        a, b = split(R[t], ~z+k); R[t] = a; pull(t); P[t] = -1
        if ~b: P[b] = -1
        return t, b
def _rank(i):
    z = cnt(L[i])+1; q = i
    while ~P[q]:
        p = P[q]
        if R[p] == q: z += cnt(L[p])+1
        q = p
    return z
def rank(T, v):
    if v not in M or not M[v]: return -1
    return _rank(M[v][-1])
def erase(T, v):
    if v not in M or not M[v]: return T
    i = M[v].pop()
    if not M[v]: del M[v]
    r = _rank(i); t1, t2 = split(T, r-1); t2, t3 = split(t2, 1)
    return merge(t1, t3)
def select(T, k):
    q = T
    while q >= 0:
        z = cnt(L[q])+1
        if k < z: q = L[q]
        elif k == z: return V[q]
        else: k -= z; q = R[q]
    return -1
def predecessor(T, v):
    r = rank(T, v)
    if r <= 1: return -1
    return select(T, r-1)
def successor(T, v):
    r = rank(T, v)
    if r < 1 or r >= cnt(T): return -1
    return select(T, r+1)
def same(i, q):
    return DU[i]*q.v+CN[i]*q.d == q.u*DV[i]
def cmp(i, j, vs):
    n, d = vs.v, vs.d; q = (DU[i]*n+CN[i]*d)*DV[j]-(DU[j]*n+CN[j]*d)*DV[i]
    if q: return -1 if q < 0 else 1
    q = DU[i]*DV[j]-DU[j]*DV[i]
    if q: return -1 if q < 0 else 1
    return -1 if i < j else 1 if i > j else 0
def splitc(t, i, vs):
    if t < 0: return -1, -1
    if cmp(i, V[t], vs) < 0:
        a, b = splitc(L[t], i, vs); L[t] = b; pull(t); P[t] = -1
        if ~a: P[a] = -1
        return a, t
    else:
        a, b = splitc(R[t], i, vs); R[t] = a; pull(t); P[t] = -1
        if ~b: P[b] = -1
        return t, b
def insert(T, v, vs):
    a, b = splitc(T, v, vs); return merge(merge(a, node(v)), b)
def intersect(a, b):
    x1, y1, x2, y2, _ = S[a]; x3, y3, x4, y4, _ = S[b]
    A = y2-y1; B = x1-x2; C0 = A*x1-(x2-x1)*y1; D = y4-y3; E = x3-x4; F = D*x3-(x4-x3)*y3; det = A*E-B*D
    if det == 0:
        pts = []
        for x, y in ((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4):
                if not pts or pts[-1] != (x, y): pts.append((x, y))
        if len(pts) == 1: x, y = pts[0]; return x, y, 1
        return
    xn = C0*E-B*F; yn = A*F-C0*D
    if det < 0: det = -det; xn = -xn; yn = -yn
    if min(x1, x2)*det <= xn <= max(x1, x2)*det and min(y1, y2)*det <= yn <= max(y1, y2)*det and min(x3, x4)*det <= xn <= max(x3, x4)*det and min(y3, y4)*det <= yn <= max(y3, y4)*det: return xn, yn, det
def addz(A, z=None):
    A = set(A)
    if len(A) < 2: return
    if z is None: z = intersect(*[*A][:2])
    if z is None: return
    x, y, d = z; g = gcd(gcd(abs(x), abs(y)), d); x //= g; y //= g; d //= g; q = (x, y, d)
    if q in ZM: Z[ZM[q]][1].update(A)
    else: ZM[q] = len(Z); Z.append(((x/d, y/d), A))
def find(a, b):
    if a < 0 or b < 0: return
    if a == b or not AC[a] or not AC[b]: return
    if a > b: pr = (b, a)
    else: pr = (a, b)
    if pr in SN: return
    z = intersect(a, b)
    if z is None: return SN.add(pr)
    x, y, d = z; qk = QK(B0*y+x, B0*x-y, d); SN.add(pr)
    if qk < ck: return
    if qk == ck: addz((a, b), z); return
    heappush(Q, (qk, 1, pr[0], pr[1]))
Q = []; Z = []; ZM = {}
Mx = max(max(x1, x2) for x1, y1, x2, y2 in G); mx = min(min(x1, x2) for x1, y1, x2, y2 in G)
My = max(max(y1, y2) for x1, y1, x2, y2 in G); my = min(min(y1, y2) for x1, y1, x2, y2 in G)
B0 = max(Mx-mx, My-my, 1)+1; S = []; AC = array('B', [0]*N); root = -1; U1 = [0]*N; V1 = [0]*N; U2 = [0]*N; V2 = [0]*N; DU = [0]*N; DV = [0]*N; CN = [0]*N
for i in range(N):
    x1, y1, x2, y2 = G[i]
    if y1 > y2 or (y1 == y2 and x1 > x2): x1, y1, x2, y2 = x2, y2, x1, y1
    S += [(x1, y1, x2, y2, i)]; u1 = B0*x1-y1; v1 = B0*y1+x1; u2 = B0*x2-y2; v2 = B0*y2+x2
    if v1 > v2: u1, v1, u2, v2 = u2, v2, u1, v1
    U1[i] = u1; V1[i] = v1; U2[i] = u2; V2[i] = v2; du = u2-u1; dv = v2-v1; DU[i] = du; DV[i] = dv; CN[i] = dv*u1-du*v1
for i in range(N): Q.append((QK(V1[i], U1[i]), 0, i, -1)); Q.append((QK(V2[i], U2[i]), 2, i, -1))
heapify(Q); SN = set(); RP = set(); cu = cv = 0; ck = (0, 0)
while Q:
    ck, ty, a, b = heappop(Q); ev = [(ty, a, b)]
    while Q and Q[0][0] == ck: _, t, aa, bb = heappop(Q); ev.append((t, aa, bb))
    ss = set(); ee = set(); cc = set()
    for t, a, b in ev:
        if t == 0: ss.add(a)
        elif t == 2: ee.add(a)
        elif AC[a] and AC[b]: cc.add(a); cc.add(b)
    for i in ss: root = insert(root, i, ck); AC[i] = 1
    zz = ss|ee|cc
    if zz:
        i = next(iter(zz))
        while 1:
            p = predecessor(root, i)
            if p < 0 or not same(p, ck): break
            zz.add(p); i = p
        i = next(iter(zz))
        while 1:
            p = successor(root, i)
            if p < 0 or not same(p, ck): break
            zz.add(p); i = p
    if len(zz) > 1: addz(zz)
    bb = set()
    for i in (rr:=zz-ss):
        if not AC[i]: continue
        p = predecessor(root, i); s = successor(root, i)
        if p >= 0 and p not in rr: bb.add(p)
        if s >= 0 and s not in rr: bb.add(s)
    for i in rr:
        if AC[i]: root = erase(root, i); AC[i] = 0
    for i in (add:=zz-ee):
        if not AC[i]: root = insert(root, i, ck); AC[i] = 1
    for i in bb|add:
        if AC[i]: find(i, predecessor(root, i)); find(i, successor(root, i))

# report all intersections
for i, (p, z) in enumerate(sorted(Z, key=lambda u: u[0]), 1):
    print('Intersection', i)
    print('Point:', p)
    print('Segments involved:', z)
    print()