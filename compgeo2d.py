from math import *

# ax+by+c=0 passes (x1,y1) and (x2,y2)
def make_line(x1, y1, x2, y2):
    return y2-y1, x1-x2, (x2-x1)*y1-(y2-y1)*x1

def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

def angle(a, o, b):
    v1, v2 = (a[0]-o[0], a[1]-o[1]), (b[0]-o[0], b[1]-o[1])
    return acos((v1[0]*v2[0]+v1[1]*v2[1])/(hypot(*v1)*hypot(*v2)))

def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])

# Returns the point/segment of intersection
def intersect(s1, s2):
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

# Use ray intersection
def pip2(p, poly):
    if not poly: return False
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-9: return True
    seg = (p, (p[0] + 1e9, p[1] + 1e9 + 7))
    return bool(sum(bool(intersect(seg, (poly[i], poly[i+1]))) for i in range(len(poly)-1)) % 2)

# Graham scan
def chull(pts):
    if len(pts) < 3: return pts
    pts, n = sorted(pts), len(pts)
    upper, lower = pts[:2], pts[-1:-3:-1]
    for i in range(2, n):
        while len(upper) > 1 and not ccw(upper[-2], upper[-1], pts[i]): upper.pop()
        upper.append(pts[i])
    for i in range(n-2, -1, -1):
        while len(lower) > 1 and not ccw(lower[-2], lower[-1], pts[i]): lower.pop()
        lower.append(pts[i])
    return upper[:-1] + lower[:-1]

# Assumes {*chull(poly)} == {*poly}
def area(poly):
    a, n = 0, len(poly)
    for i in range(n): a += poly[i][0]*poly[(i+1)%n][1] - poly[i][1]*poly[(i+1)%n][0]
    return abs(a)/2

# Assumption: px and py are list of complex numbers, px sorted by x, py sorted by y
def closest_pair(px, py):
    if len(px) < 40: # just brute-force it
        d = 1e9
        for i in range(len(px)-1):
            for j in range(i+1, len(px)):
                if (d2:=abs(px[i] -px[j])) < d: d, p1, p2 = d2, px[i], px[j]
        return d, p1, p2
    mid = len(px)//2
    xmid = px[mid].real
    py1, py2 = [], []
    for i in py:
        if i.real < xmid: py1.append(i)
        else: py2.append(i)
    d, p1, p2 = min(closest_pair(px[:mid], py1), closest_pair(px[mid:], py2))
    q = [i for i in py if abs(i.real - xmid) < d]
    for i in range(len(q)-1):
        for j in range(i+1, min(i+7, len(q))):
            if (d2:=abs(q[i] - q[j])) < d: d, p1, p2 = d2, q[i], q[j]
            else: break
    return d, p1, p2

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