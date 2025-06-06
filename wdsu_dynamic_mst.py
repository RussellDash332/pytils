# https://codeforces.com/blog/entry/130107
class WDSU:
    def __init__(s, N):
        s.p = [*range(N)]; s.w = [10**9]*N; s.s = [1]*N
    def cm(s, v, w=10**9-1):
        while s.w[v] <= w:
            while s.w[s.p[v]] <= s.w[v]: s.s[s.p[v]] -= s.s[v]; s.p[v] = s.p[s.p[v]]
            v = s.p[v]
        return v
    def dc(s, v):
        if s.p[v] != v: s.dc(s.p[v]); s.s[s.p[v]] -= s.s[v]
    def co(s, v, w=10**9-1):
        while s.w[v] <= w: s.s[s.p[v]] += s.s[v]; v = s.p[v]
        return v
    def me(s, u, v):
        if s.cm(u) != s.cm(v): return -1
        while s.p[u] != v and s.p[v] != u:
            if s.w[u] < s.w[v]: u = s.p[u]
            else: v = s.p[v]
        if s.p[u] == v: return u
        return v
    def lk(s, u, v, w):
        s.dc(u); s.dc(v)
        while u != v:
            u = s.co(u, w); v = s.co(v, w)
            if s.s[u] < s.s[v]: u, v = v, u
            s.p[v], u = u, s.p[v]; s.w[v], w = w, s.w[v]
        s.co(v)
    def add(s, u, v, w): # add an edge (u, v) with weight w
        p = s.me(u, v)
        if p == -1: s.lk(u, v, w)
        elif s.w[p] > w:
            q = p; z = s.w[p]
            while s.p[q] != q: q = s.p[q]; s.s[q] -= s.s[p]
            s.p[p] = p; s.w[p] = 10**9; s.lk(u, v, w)
            return z