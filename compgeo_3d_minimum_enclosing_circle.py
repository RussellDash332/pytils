from random import *

def dist(a, b, c):
    return (a*a+b*b+c*c)**0.5

# minimum enclosing circle
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

def cross_util(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def cross(a, b, c):
    return cross_util((b[0]-a[0], b[1]-a[1], b[2]-a[2]), (c[0]-a[0], c[1]-a[1], c[2]-a[2]))

def circumcenter(a, b, c):
    x = (c[0]-a[0], c[1]-a[1], c[2]-a[2])
    y = (b[0]-a[0], b[1]-a[1], b[2]-a[2])
    s1 = dist(*x); s2 = dist(*y)
    c = cross_util(x, y); d = (-c[0], -c[1], -c[2]); e = 2*(c[0]**2+c[1]**2+c[2]**2)
    p = cross_util(d, y); q = cross_util(c, x)
    return (a[0]+s1*s1/e*p[0]+s2*s2/e*q[0] , a[1]+s1*s1/e*p[1]+s2*s2/e*q[1], a[2]+s1*s1/e*p[2]+s2*s2/e*q[2])

# alternate version - recursive + circumcenter
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
    print(mec([(3, 2, -5), (-3, 8, -5), (-3, 2, 1)]))
    print(mec2([(3, 2, -5), (-3, 8, -5), (-3, 2, 1)]))

    print(circumcenter((3, 2, -5), (-3, 8, -5), (-3, 2, 1)))