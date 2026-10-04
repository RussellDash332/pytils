# Sweep on a sorted set/list
# Assumption: pts are list of (x, y) points
# Can change s to SortedList as well
from bisect import *
from math import *
def closest_triple(p):
    z = (1e38, None); j = 0; s = []; p.sort(); n = len(p)
    for x, y in p:
        d = z[0]/2
        while j < n and x-p[j][0] >= d: s.remove((p[j][1], p[j][0])); j += 1
        b = bisect_left(s, (y-d, -1e38))
        for k in range(b, len(s)):
            if s[k][0] > y+d: break
            e = s[k]
            for l in range(k+1, len(s)):
                if s[l][0] > y+d: break
                f = s[l]; w = hypot(x-e[1], y-e[0])+hypot(x-f[1], y-f[0])+hypot(e[1]-f[1], e[0]-f[0])
                if w < z[0]: z = (w, ((x, y), (e[1], e[0]), (f[1], f[0])))
        insort(s, (y, x))
    return z

from random import *
if __name__ == '__main__':
    # test random points
    N = randint(200, 500)
    print('Random test on', N, 'points')

    P = set()
    while len(P) < N: P.add((randint(-10**6, 10**6), randint(-10**6, 10**6)))
    P = [*P]

    # compare with O(N^3) brute-force
    z = (1e38, None)
    def dist(i, j):
        return hypot(P[i][0]-P[j][0], P[i][1]-P[j][1])
    for i in range(N):
        for j in range(i):
            b = dist(i, j)
            if b > z[0]: continue
            for k in range(j):
                p = b+dist(j, k)+dist(k, i)
                if p < z[0]: z = (p, t:=(P[i], P[j], P[k]))
    print('Brute-force:', z[0], sorted(t))

    d, t = closest_triple(P)
    print('Sweep-line: ', d, sorted(t))