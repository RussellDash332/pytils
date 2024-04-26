from math import *
from random import *

def dist(a, b, c):
    return (a*a+b*b+c*c)**0.5

def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def cross_util(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def cross(a, b, c):
    return cross_util((b[0]-a[0], b[1]-a[1], b[2]-a[2]), (c[0]-a[0], c[1]-a[1], c[2]-a[2]))

# O(n^2) KACTL, no four points are coplanar
def chull(A):
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
    return F

# projection from p to segment ab
def proj(p, s):
    a, b = s
    d = (b[0]-a[0], b[1]-a[1], b[2]-a[2])
    n = dist(*d)
    u = (d[0]/n, d[1]/n, d[2]/n)
    x = dot((p[0]-a[0], p[1]-a[1], p[2]-a[2]), u)
    return (a[0]+u[0]*x, a[1]+u[1]*x, a[2]+u[2]*x)

# projectiom from p to plane q
def proj2(p, q):
    a, b, c = q
    t = cross(a, b, c)
    n = dist(*t)
    u = (t[0]/n, t[1]/n, t[2]/n)
    x = dot(p, u)-dot(a, u)
    return (p[0]-u[0]*x, p[1]-u[1]*x, p[2]-u[2]*x)

# x can be a line or a plane
def perp_dist(p, x):
    if len(x) == 2: q = proj(p, x)
    else: q = proj2(p, x)
    return dist(p[0]-q[0], p[1]-q[1], p[2]-q[2])

# alternative method for distance from p to segment ab
def alt_dist(p, s):
    a, b = s
    if dot((a[0]-p[0], a[1]-p[1], a[2]-p[2]), (a[0]-b[0], a[1]-b[1], a[2]-b[2])) <= 0: return dist(a[0]-p[0], a[1]-p[1], a[2]-p[2])
    if dot((b[0]-p[0], b[1]-p[1], b[2]-p[2]), (b[0]-a[0], b[1]-a[1], b[2]-a[2])) <= 0: return dist(b[0]-p[0], b[1]-p[1], b[2]-p[2])
    return dist(*cross(p, a, b))/dist(a[0]-b[0], a[1]-b[1], a[2]-b[2])

# line-plane intersection
def lpx(l, p):
    c = cross(p[0], p[1], p[2])
    n = dist(*c)
    u = (c[0]/n, c[1]/n, c[2]/n)
    x = dot(l[0], u)-dot(p[0], u)
    y = dot(l[1], u)-dot(p[0], u)
    return ((l[0][0]*y-l[1][0]*x)/(y-x), (l[0][1]*y-l[1][1]*x)/(y-x), (l[0][2]*y-l[1][2]*x)/(y-x))

def circumcenter(a, b, c):
    x = (c[0]-a[0], c[1]-a[1], c[2]-a[2])
    y = (b[0]-a[0], b[1]-a[1], b[2]-a[2])
    s1 = dist(*x); s2 = dist(*y)
    c = cross_util(x, y); d = (-c[0], -c[1], -c[2]); e = 2*(c[0]**2+c[1]**2+c[2]**2)
    p = cross_util(d, y); q = cross_util(c, x)
    return (a[0]+s1*s1/e*p[0]+s2*s2/e*q[0] , a[1]+s1*s1/e*p[1]+s2*s2/e*q[1], a[2]+s1*s1/e*p[2]+s2*s2/e*q[2])

# minimum enclosing points
def mec(p):
    shuffle(p); o = p[0]; r = 0; eps = 1+1e-9
    for i in range(len(p)):
        if dist(o[0]-p[i][0], o[1]-p[i][1], o[2]-p[i][2]) <= r*eps: continue
        o = p[i]; r = 0
        for j in range(i):
            if dist(o[0]-p[j][0], o[1]-p[j][1], o[2]-p[j][2]) <= r*eps: continue
            o = ((p[i][0]+p[j][0])/2, (p[i][1]+p[j][1])/2, (p[i][2]+p[j][2])/2)
            r = dist(o[0]-p[i][0], o[1]-p[i][1], o[2]-p[i][2])
            for k in range(j):
                if dist(o[0]-p[k][0], o[1]-p[k][1], o[2]-p[k][2]) <= r*eps: continue
                o = circumcenter(p[i], p[j], p[k])
                r = dist(o[0]-p[i][0], o[1]-p[i][1], o[2]-p[i][2])
    return o, r

def mec2(p):
    def helper(n, k):
        if k >= 3:
            c = circumcenter(p[n-1], p[n-2], p[n-3])
            r = dist(c[0]-p[n-1][0], c[1]-p[n-1][1], c[2]-p[n-1][2])
            print(c, r)
            return c, r
        if n == 1: return p[0], 0
        if n == 2: return ((p[0][0]+p[1][0])/2, (p[0][1]+p[1][1])/2, (p[0][2]+p[1][2])/2), dist(p[0][0]-p[1][0], p[0][1]-p[1][1], p[0][2]-p[1][2])/2
        i = randint(0, n-k-1)
        p[i], p[n-1-k] = p[n-1-k], p[i]; p[n-1-k], p[n-1] = p[n-1], p[n-1-k]
        o, r = helper(n-1, k)
        p[n-1-k], p[n-1] = p[n-1], p[n-1-k]; p[i], p[n-1-k] = p[n-1-k], p[i]
        if dist(p[i][0]-o[0], p[i][1]-o[1], p[i][2]-o[2]) <= r+1e-9: return o, r
        p[i], p[n-1-k] = p[n-1-k], p[i]
        x = helper(n, k+1)
        p[i], p[n-1-k] = p[n-1-k], p[i]
        return x
    return helper(len(p), 0)

if __name__ == '__main__':
    P = [(1, 0, 0), (1, 1, 0), (0, 0, 0), (0, 0, 1)]
    print(chull(P))

    P = [(0, 0, 0), (100, 0, 0), (0, 100, 0), (0, 0, 100), (20, 20, 20), (30, 20, 10)]
    print(chull(P))

    print(alt_dist((4, 2, 1), ((1, 0, 1), (1, 2, 0)))) # sqrt(9.8)
    print(perp_dist((4, 2, 1), ((1, 0, 1), (1, 2, 0)))) # sqrt(9.8)
    x, y, z = proj((4, 2, 1), ((1, 0, 1), (1, 2, 0)))
    print(dist(4-x, 2-y, 1-z))

    print(perp_dist((1, 1, 1), ((0, 0, 0), (-1, 2, -1), (5, 2, -3)))) # sqrt(126)/7
    x, y, z = proj2((1, 1, 1), ((0, 0, 0), (-1, 2, -1), (5, 2, -3)))
    print(dist(1-x, 1-y, 1-z))

    print((x, y, z))
    print(lpx(((1, 1, 1), (-2, -5, -8)), ((0, 0, 0), (-1, 2, -1), (5, 2, -3))))

    print(circumcenter((3, 2, -5), (-3, 8, -5), (-3, 2, 1)))

    print(mec([(3, 2, -5), (-3, 8, -5), (-3, 2, 1)]))
    print(mec2([(3, 2, -5), (-3, 8, -5), (-3, 2, 1)]))