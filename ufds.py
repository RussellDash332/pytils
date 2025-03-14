class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]

# with rollback
class UFDS:
    def __init__(s, n):
        s.p = [-1]*n; s.o = []
    def find(s, u):
        while s.p[u] > -1: u = s.p[u]
        return u
    def union(s, u, v):
        if (u:=s.find(u)) != (v:=s.find(v)):
            if s.p[u] > s.p[v]: u, v = v, u
            s.o.append((v, s.p[v])); s.p[u] += s.p[v]; s.p[v] = u
    def undo(s):
        if s.o: v, x = s.o.pop(); s.p[s.p[v]] -= x; s.p[v] = x