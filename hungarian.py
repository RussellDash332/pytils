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

# Example from https://brilliant.org/wiki/hungarian-matching/
print(hungarian([
    [108, 125, 150],
    [150, 135, 175],
    [122, 148, 250]
]))

# col > row?
print(hungarian([
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