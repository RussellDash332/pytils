from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

V = 5
g = [[] for _ in range(V)]
match, mcbm = [-1]*V, 0
free = set()
nfree = len(free)

for l in list(free):
    if (candidates:=[r for r in g[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
for f in free: vis = [0]*nfree; mcbm += aug(f)

print(mcbm)