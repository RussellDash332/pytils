from math import *
EPS = 1e-11

def clamp(x):
    return max(min(x, 1), -1)

def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def vadd(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def vsub(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def unit(a):
    z = hypot(*a); return tuple(v/z for v in a)

def great_circle_distance(p1, p2):
    r = hypot(*p1); u1, u2 = unit(p1), unit(p2); la1, lo1 = asin(clamp(u1[2])), atan2(u1[1], u1[0]); la2, lo2 = asin(clamp(u2[2])), atan2(u2[1], u2[0]); return r*acos(clamp(sin(la1)*sin(la2)+cos(la1)*cos(la2)*cos(lo2-lo1)))

def ang(a, b):
    return atan2(hypot(*cross(a, b)), dot(a, b))

def arc(a, b, x):
    return 0 if abs(dot(x, c:=cross(a, b))) > EPS*hypot(*c) else abs(ang(a, x)+ang(x, b)-ang(a, b)) < EPS

def perp_dist(p, a, b):
    c = unit(cross(a, b)); k = clamp(dot(p, c)); return abs(asin(k))

def proj(p, a, b):
    c = unit(cross(a, b)); k = clamp(dot(p, c)); x = vsub(p, [k*v for v in c]); xx = hypot(*x); return tuple(v/xx for v in x) if xx > EPS else a

def pipgc(q, P):
    n = len(P)
    for i in range(n):
        if arc(P[i], P[i-1], q): return 1 # on the polygon?
    for i in range(n):
        m = unit(vadd(a:=P[i-1], b:=P[i])); nm = unit(cross(a, b)); cs = cos(EPS); sn = sin(EPS); rn = cross(r:=vsub([cs*v for v in m], [sn*v for v in nm]), q); z = hypot(*rn)
        if z < EPS: continue
        if any(arc(r, q, p) for p in P): continue
        cz = 0; rn = tuple(v/z for v in rn)
        for j in range(n):
            x = cross(rn, cross(a:=P[j-1], b:=P[j])); z = hypot(*x)
            if z > EPS: x = tuple(v/z for v in x); nx = (-x[0], -x[1], -x[2]); cz ^= (arc(r, q, x) and arc(a, b, x)) or (arc(r, q, nx) and arc(a, b, nx))
        return cz == 1
    return 0

if __name__ == '__main__':
    SG = (-1521.55836261, 6184.81969242, 150.32986427)
    JKT = (-1835.39054796, 6061.88046755, -689.04351052)
    print('Singapore to Jakarta distance:', great_circle_distance(SG, JKT)) # about 900km, which is accurate

    # Tested in https://open.kattis.com/problems/marooned
    P1 = [
        (-2733.658938, 4005.128211, 4132.275139),
        (-4775.862665, -1082.528871, 4075.402808),
        (447.156539, -4918.721930, 4024.408852),
        (4433.618367, 1710.109941, 4243.606151),
        (1778.729143, 5907.921798, 1588.151021)
    ]
    P2 = [
        (3900.268462, -4879.058077, 1253.929506),
        (5845.673734, -771.280493, 2413.061541),
        (3682.390263, -877.940063, 5124.340367),
        (-967.569723, -3996.218857, 4866.588608),
        (-105.699984, -6270.499063, 1122.189832),
        (2913.818439, -4997.307324, -2669.498570),
        (6011.437191, 2003.809064, 661.069691),
        (3208.348180, 1858.558946, 5180.917062),
        (6288.929998, -504.340000, 885.800000)
    ]
    Q1 = (3067.758708, -3067.758708, 4665.549702)
    Q2 = (3541.698871, -4520.488559, 2758.839121)

    p1 = [unit(p) for p in P1]
    p2 = [unit(p) for p in P2]
    q1 = unit(Q1)
    q2 = unit(Q2)

    print(pipgc(q1, p1)) # first sample input, False
    print(pipgc(q2, p2)) # second sample input, True

    # Edge 2->3 is our first sample input
    r1 = hypot(*Q1)
    for i in range(len(p1)):
        a, b = p1[i-1], p1[i]; x = proj(q1, a, b)
        if arc(a, b, x): d = perp_dist(q1, a, b)
        else: d = min(ang(q1, a), ang(q1, b))
        t = tuple(v*r1 for v in x)
        print(f"Edge ({i-1} -> {i}):")
        print(f"  Projection (unit): {x}")
        print(f"  Projection (3D):   {t}")
        print(f"  Angular Distance:  {d} rad")
        print(f"  Surface Distance:  {d*r1}")