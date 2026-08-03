# Also known as Kuhn-Munkres
from array import *
def hungarian(mat):
    if len(mat) > len(mat[0]): mat = [*map(list, zip(*mat))]
    INF = 10**9; n = len(mat)+1; m = len(mat[0])+1; ans = 0; ii = [0]*max(m, n)
    mtc = array('i', ii); u = array('i', ii); v = array('i', ii); w = array('i', ii); c = 0
    mat = [array('i', ii), *(array('i', [0]+r) for r in mat)]
    for i in range(1, n):
        mtc[0] = i; mi = array('i', [INF]*m); vis = array('i', ii)
        while 1:
            vis[c] = 1; d = INF; c2 = 0
            for j in range(1, m):
                if vis[j]: continue
                if (cur:=mat[mtc[c]][j]-u[mtc[c]]-v[j]) < mi[j]: mi[j] = cur; w[j] = c
                if mi[j] < d: d = mi[j]; c2 = j
            for j in range(m):
                if vis[j]: u[mtc[j]] += d; v[j] -= d
                else: mi[j] -= d
            if mtc[(c:=c2)] == 0: break
        while 1:
            mtc[c] = mtc[w[c]]
            if (c:=w[c]) == 0: break
    for i in range(1, m):
        if mtc[i]: ans += mat[mtc[i]][i]
    return ans

# Credits: Jeremy Lim
# Linear Assignment Problem using Jonker-Volgenant algorithm
def lapjv(mat):
    if len(mat) > len(mat[0]): mat = [*map(list, zip(*mat))]
    n, m = len(mat), len(mat[0]); D = [0]*m; P = [0]*m; mtc = [-1]*n; cm = [-1]*m; C = [*range(m)]; pr = [0]*m; d = 0
    for i in range(n):
        for c in range(m): D[c] = mat[i][c]-P[c]; pr[c] = i
        s = t = x = z = 0
        while z^1:
            if s == t:
                x = s; d = D[C[t]]; t += 1
                for j in range(t, m):
                    if d < D[c:=C[j]]: continue
                    if d > D[c]: d = D[c]; t = s
                    C[j], C[t] = C[t], C[j]; t += 1
                for j in range(s, t):
                    if cm[c:=C[j]] < 0: z = 1; break
                if z: break
            r = cm[e:=C[s]]; s += 1
            for j in range(t, m):
                if D[c:=C[j]] <= (v:=mat[r][c]-mat[r][e]+P[e]-P[c]+d): continue
                D[c] = v; pr[c] = r
                if v == d:
                    if cm[c] < 0: z = 1; break
                    C[j], C[t] = C[t], C[j]; t += 1
            if z: break
        for j in range(x): P[C[j]] += D[C[j]]-d
        r = -1
        while r != i: r = cm[c] = pr[c]; c, mtc[r] = mtc[r], c
    return sum(mat[i][mtc[i]] for i in range(n))

if __name__ == '__main__':
    # Example from https://brilliant.org/wiki/hungarian-matching/
    print(hungarian([
        [108, 125, 150],
        [150, 135, 175],
        [122, 148, 250]
    ]))
    print(lapjv([
        [108, 125, 150],
        [150, 135, 175],
        [122, 148, 250]
    ]))

    # col > row?
    print(hungarian([
        [1, 2, 3],
        [2, 300, 4]
    ]))
    print(lapjv([
        [1, 2, 3],
        [2, 300, 4]
    ]))

    # row > col? need to transpose!
    print(hungarian([
        [1, 2, 13],
        [2, 3, 34],
        [43, 4, 54],
        [4, 5, 6]
    ]))
    print(lapjv([
        [1, 2, 13],
        [2, 3, 34],
        [43, 4, 54],
        [4, 5, 6]
    ]))

    print(hungarian([
        [10, 15, 20],
        [5, 2, 8],
        [12, 9, 4]
    ]))
    print(lapjv([
        [10, 15, 20],
        [5, 2, 8],
        [12, 9, 4]
    ]))

    from random import *
    from time import *

    def test(a, b):
        n = randint(500, 700); m = randint(500, 700)
        mat = [[randint(a, b) for _ in range(m)] for _ in range(n)]
        print('Size:', (n, m))
        print('Cost range:', [a, b])
        t = perf_counter(); print('Hungarian:', hungarian(mat), 'in', round(perf_counter()-t, 5), 'seconds')
        t = perf_counter(); print('LAPJV:    ', lapjv(mat), 'in', round(perf_counter()-t, 5), 'seconds')

    test(1, 1)
    test(1, 10)
    test(1, 10**6)