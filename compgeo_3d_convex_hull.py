# Represent a point as a tuple (x, y, z) and a polyhedron as a list of points
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

if __name__ == '__main__':
    P = [(1, 0, 0), (1, 1, 0), (0, 0, 0), (0, 0, 1)]
    print(chull(P))

    P = [(0, 0, 0), (100, 0, 0), (0, 100, 0), (0, 0, 100), (20, 20, 20), (30, 20, 10)]
    print(chull(P))