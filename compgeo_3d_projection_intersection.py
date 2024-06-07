from math import *

def dist(a, b, c):
    return (a*a+b*b+c*c)**0.5

def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def cross_util(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def cross(a, b, c):
    return cross_util((b[0]-a[0], b[1]-a[1], b[2]-a[2]), (c[0]-a[0], c[1]-a[1], c[2]-a[2]))

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

if __name__ == '__main__':
    print(alt_dist((4, 2, 1), ((1, 0, 1), (1, 2, 0)))) # sqrt(9.8)
    print(perp_dist((4, 2, 1), ((1, 0, 1), (1, 2, 0)))) # sqrt(9.8)
    x, y, z = proj((4, 2, 1), ((1, 0, 1), (1, 2, 0)))
    print(dist(4-x, 2-y, 1-z))

    print(perp_dist((1, 1, 1), ((0, 0, 0), (-1, 2, -1), (5, 2, -3)))) # sqrt(126)/7
    x, y, z = proj2((1, 1, 1), ((0, 0, 0), (-1, 2, -1), (5, 2, -3)))
    print(dist(1-x, 1-y, 1-z))

    print((x, y, z))
    print(lpx(((1, 1, 1), (-2, -5, -8)), ((0, 0, 0), (-1, 2, -1), (5, 2, -3))))