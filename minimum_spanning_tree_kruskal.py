n = 1
g = [{} for _ in range(n)]

# Kruskal's algorithm
class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]
el = []; mst = []; u = UFDS(n)
for a in range(n):
    for b in g[a]: el.append((g[a][b], a, b))
for w, a, b in sorted(el):
    if u.find(a) != u.find(b): u.union(a, b), mst.append((a, b, w))
print(mst)