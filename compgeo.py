from math import *

def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]

def norm(a):
    return hypot(*a)

def angle(a, o, b):
    v1, v2 = (a[0]-o[0], a[1]-o[1]), (b[0]-o[0], b[1]-o[1])
    return acos(dot(v1, v2)/(norm(v1)*norm(v2)))

def ccw(p, q, r):
    v1, v2 = (q[0]-p[0], q[1]-p[1]), (r[0]-p[0], r[1]-p[1])
    return cross(v1, v2) > 0

def intersect(s1, s2): # return the point/segment of intersection
    (p1, p2), (p3, p4) = s1, s2
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1
    d, e, f = y4-y3, x3-x4, (y4-y3)*x3 - (x4-x3)*y3
    if a == b == 0: return ((x1, y1) if (x1, y1) == (x3, y3) else None) if d == e == 0 else ((x1, y1) if d*x1 + e*y1 == f and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4) else None)
    elif d == e == 0: return (x3, y3) if a*x3 + b*y3 == c and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2) else None
    else:
        det = b*d-a*e
        if det:
            x, y = (b*f-c*e)/det, (c*d-a*f)/det
            return (x, y) if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4) else None
        else:
            if a*f != c*d or b*f != c*e: return None
            else:
                p, q = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))
                r, s = min((x3, y3), (x4, y4)), max((x3, y3), (x4, y4))
                if (p, q) == (r, s):    i1, i2 = p, q
                elif p <= r <= q:       i1, i2 = r, min(q, s)
                elif r <= p <= s:       i1, i2 = p, min(s, q)
                else:                   i1 = i2 = None
                if i1 == i2 and i1 != None: return i1
                elif i1:                    return (i1, i2)
                else:                       return None

def pip(p, poly):
    if not poly: return False
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-9: return True
    s = sum((2*ccw(p, poly[i], poly[i+1])-1) * angle(poly[i], p, poly[i+1]) for i in range(len(poly)-1))
    return abs(abs(s) - 2*pi) < 1e-9

def pip2(p, poly):
    if not poly: return False
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-9: return True
    seg = (p, (p[0] + 1e9, p[1] + 1e9 + 7))
    return bool(sum(bool(intersect(seg, (poly[i], poly[i+1]))) for i in range(len(poly)-1)) % 2)

def chull(pts):
    n, k = len(pts), 0
    pts = sorted(pts)
    h = [None]*(2*n)
    for i in range(n):
        while k >= 2 and not ccw(h[k-2], h[k-1], pts[i]): k -= 1
        h[k] = pts[i]; k += 1
    t = k+1
    for i in range(n-2, -1, -1):
        while k >= t and not ccw(h[k-2], h[k-1], pts[i]): k -= 1
        h[k] = pts[i]; k += 1
    while h[-1] == None: h.pop()
    return h

if __name__ == '__main__':
    shape = [(1, 1), (3, 3), (9, 1), (12, 4), (9, 7), (1, 7)]
    shape.append(shape[0])
    print(pip((3, 2), shape), pip2((3, 2), shape))
    print(pip((3, 3), shape), pip2((3, 3), shape))
    print(pip((5, 7), shape), pip2((5, 7), shape))
    print(pip((3, 4), shape), pip2((3, 4), shape))
    print(pip((8, -4), shape), pip2((8, -4), shape))
    print(shape)
    print(chull(shape))