from math import *

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
    n = hypot(*d)
    u = (d[0]/n, d[1]/n, d[2]/n)
    x = dot((p[0]-a[0], p[1]-a[1], p[2]-a[2]), u)
    return (a[0]+u[0]*x, a[1]+u[1]*x, a[2]+u[2]*x)

# projectiom from p to plane q
def proj2(p, q):
    a, b, c = q
    t = cross(a, b, c)
    n = hypot(*t)
    u = (t[0]/n, t[1]/n, t[2]/n)
    x = dot(p, u)-dot(a, u)
    return (p[0]-u[0]*x, p[1]-u[1]*x, p[2]-u[2]*x)

# x can be a line or a plane
def perp_dist(p, x):
    if len(x) == 2: q = proj(p, x)
    else: q = proj2(p, x)
    return hypot(p[0]-q[0], p[1]-q[1], p[2]-q[2])

# alternative method for distance from p to segment ab
def alt_dist(p, s):
    a, b = s
    if dot((a[0]-p[0], a[1]-p[1], a[2]-p[2]), (a[0]-b[0], a[1]-b[1], a[2]-b[2])) <= 0: return hypot(a[0]-p[0], a[1]-p[1], a[2]-p[2])
    if dot((b[0]-p[0], b[1]-p[1], b[2]-p[2]), (b[0]-a[0], b[1]-a[1], b[2]-a[2])) <= 0: return hypot(b[0]-p[0], b[1]-p[1], b[2]-p[2])
    return hypot(*cross(p, a, b))/hypot(a[0]-b[0], a[1]-b[1], a[2]-b[2])

# line-plane intersection
def lpx(l, p):
    c = cross(p[0], p[1], p[2])
    n = hypot(*c)
    u = (c[0]/n, c[1]/n, c[2]/n)
    x = dot(l[0], u)-dot(p[0], u)
    y = dot(l[1], u)-dot(p[0], u)
    return ((l[0][0]*y-l[1][0]*x)/(y-x), (l[0][1]*y-l[1][1]*x)/(y-x), (l[0][2]*y-l[1][2]*x)/(y-x))

if __name__ == '__main__':
    P = [(1, 0, 0), (1, 1, 0), (0, 0, 0), (0, 0, 1)]
    print(chull(P))

    P = [(0, 0, 0), (100, 0, 0), (0, 100, 0), (0, 0, 100), (20, 20, 20), (30, 20, 10)]
    print(chull(P))

    print(alt_dist((4, 2, 1), ((1, 0, 1), (1, 2, 0)))) # sqrt(9.8)
    print(perp_dist((4, 2, 1), ((1, 0, 1), (1, 2, 0)))) # sqrt(9.8)
    x, y, z = proj((4, 2, 1), ((1, 0, 1), (1, 2, 0)))
    print(hypot(4-x, 2-y, 1-z))

    print(perp_dist((1, 1, 1), ((0, 0, 0), (-1, 2, -1), (5, 2, -3)))) # sqrt(126)/7
    x, y, z = proj2((1, 1, 1), ((0, 0, 0), (-1, 2, -1), (5, 2, -3)))
    print(hypot(1-x, 1-y, 1-z))

    print((x, y, z))
    print(lpx(((1, 1, 1), (-2, -5, -8)), ((0, 0, 0), (-1, 2, -1), (5, 2, -3))))