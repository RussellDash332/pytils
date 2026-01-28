# Faster, sweep on a sorted set/list
# Assumption: pts are list of (x, y) points
# Can change s to SortedList as well
def closest_pair(pts):
    pts.sort(); best = (1e38, None, None); j = 0; n = len(pts); s = []
    for i in range(n):
        d = ceil(best[0]**.5); x, y = pts[i]
        while j < n and x-pts[j][0] >= d: s.remove((p[j][1], p[j][0])); j += 1
        b = bisect_left(s, (y-d, x))
        for k in range(b, min(b+5, len(s))):
            e = s[k]; new = (x-e[1])**2+(y-e[0])**2
            if new < best[0]: best = (new, (x, y), (e[1], e[0]))
        insort(s, (y, x))
    return best

# Slower divide-and-conquer, but simpler
# Assumption: px and py are list of complex numbers, px sorted by x, py sorted by y
def closest_pair(px, py):
    if len(px) < 40: # just brute-force it
        d = 1e9
        for i in range(len(px)-1):
            for j in range(i+1, len(px)):
                if (d2:=abs(px[i]-px[j])) < d: d, p1, p2 = d2, px[i], px[j]
        return d, p1, p2
    mid = len(px)//2; xmid = px[mid].real; py1, py2 = [], []
    for i in py:
        if i.real < xmid: py1.append(i)
        else: py2.append(i)
    d, p1, p2 = min(closest_pair(px[:mid], py1), closest_pair(px[mid:], py2)); q = [i for i in py if abs(i.real-xmid) < d]
    for i in range(len(q)-1):
        for j in range(i+1, min(i+7, len(q))):
            if (d2:=abs(q[i]-q[j])) < d: d, p1, p2 = d2, q[i], q[j]
            else: break
    return d, p1, p2