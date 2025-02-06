# Represent a point as a tuple of (x, y)
# Represent a polygon as a list of points

from compgeo_2d_intersect import intersect_check
from math import *

def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

def angle(a, o, b):
    v1, v2 = (a[0]-o[0], a[1]-o[1]), (b[0]-o[0], b[1]-o[1])
    return acos((v1[0]*v2[0]+v1[1]*v2[1])/(hypot(*v1)*hypot(*v2)))

def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])

def pip(p, poly):
    if not poly: return False
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-9: return True
    s = sum((2*ccw(p, poly[i], poly[i+1])-1) * angle(poly[i], p, poly[i+1]) for i in range(len(poly)-1))
    return abs(abs(s) - 2*pi) < 1e-9

# Use ray intersection and intersect_check from the other file
def pip2(p, poly):
    if not poly: return False
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-9: return True
    ray = (p, (p[0]+1e9, p[1]+1e9+7))
    return bool(sum(intersect_check(ray, (poly[i], poly[i+1])) for i in range(len(poly)-1))%2)

if __name__ == '__main__':
    shape = [(1, 1), (3, 3), (9, 1), (12, 4), (9, 7), (1, 7)]
    shape.append(shape[0])
    print(pip((3, 2), shape), pip2((3, 2), shape))
    print(pip((3, 3), shape), pip2((3, 3), shape))
    print(pip((5, 7), shape), pip2((5, 7), shape))
    print(pip((3, 4), shape), pip2((3, 4), shape))
    print(pip((8, -4), shape), pip2((8, -4), shape))
    print(shape)