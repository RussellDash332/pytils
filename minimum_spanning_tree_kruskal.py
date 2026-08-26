n = 1
g = [{} for _ in range(n)]

# Kruskal's algorithm
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
el = []; mst = []; u = UFDS(n)
for a in range(n):
    for b in g[a]: el.append((g[a][b], a, b))
for w, a, b in sorted(el):
    if u.find(a) != u.find(b): u.union(a, b), mst.append((a, b, w))
print(mst)