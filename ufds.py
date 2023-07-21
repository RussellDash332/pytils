class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]
        self.rank = [0]*N
    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find_set(i)) != (y:=self.find_set(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]