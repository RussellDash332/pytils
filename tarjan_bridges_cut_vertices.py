N = 10
G = [[1, 2], [0, 2, 3], [0, 1, 7], [1, 4, 6], [3, 5], [4, 6], [3, 5], [8, 9, 2], [9, 7], [8, 7]]

# Iterative version
T = 0; V = [0]*N; D = [-1]*N; L = [-1]*N; X = [0]*N; bridges = []; cut_vertices = []
for i in range(N):
    if not V[i]:
        S = [(2*i, -1)]
        while S:
            vs, p = S.pop(); v, s = divmod(vs, 2)
            if s&1:
                L[v] = min(L[v], L[p])
                if L[p] > D[v]: bridges.append((v, p))
                if v != i and L[p] >= D[v]: cut_vertices.append(v)
            else:
                if V[v]: S.pop(); continue
                if p != -1: X[p] += 1
                V[v] = 1; D[v] = L[v] = T; T += 1
                for to in G[v]:
                    if to == p: continue
                    if V[to]: L[v] = min(L[v], D[to])
                    else: S.append((vs^1, to)); S.append((2*to, v))
        if X[i] > 1: cut_vertices.append(v)
print(bridges)
print(cut_vertices)

# Recursive version
def dfs(v, p):
    V[v] = 1; D[v] = L[v] = T[0]; T[0] += 1; X = 0
    for to in G[v]:
        if to == p: continue
        if V[to]: L[v] = min(L[v], D[to])
        else:
            X += 1; dfs(to, v); L[v] = min(L[v], L[to])
            if L[to] > D[v]: bridges.append((v, to))
            if p != -1 and L[to] >= D[v]: cut_vertices.append(v)
    if p == -1 and X > 1: cut_vertices.append(v)
T = [0]; V = [0]*N; D = [-1]*N; L = [-1]*N; bridges = []; cut_vertices = []
for i in range(N):
    if not V[i]: dfs(i, -1)
print(bridges)
print(cut_vertices)