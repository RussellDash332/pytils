# g was put outside the function for more efficiency
def bk(r, p, x):
    if not p and not x: return len(r)
    a = 0
    for i in p: u = i; break
    for i in x: u = i; break
    for w in [*p]:
        if w in g[u]: continue
        r.add(w); a = max(a, bk(r, p&g[w], x&g[w])); r.discard(w); p.discard(w); x.add(w)
    return a

# represent undirected graph as a list of sets
g = [{1, 2}, {0, 2}, {0, 1, 3}, {2, 4, 5}, {3, 5, 6}, {3, 4, 6}, {4, 5}]
v = len(g)
print(bk(set(), {*range(v)}, set()))

g = [{1, 2}, {0, 2}, {0, 1, 3}, {2, 4, 5, 6}, {3, 5, 6}, {3, 4, 6}, {3, 4, 5}]
v = len(g)
print(bk(set(), {*range(v)}, set()))