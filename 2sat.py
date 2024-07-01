# Given N variables, create a graph with 2N vertices
# 0, 1, ..., N-1 indicating x_i
# N, N+1, ..., 2N-1 indicating -x_i

# (a v -b) ^ (-a v b) ^ (-a v -b) ^ (a v -c)
N = 3
CNF = (((0, 0), (1, 1)), ((0, 1), (1, 0)), ((0, 1), (1, 1)), ((0, 0), (2, 1)))

G = [[] for _ in range(2*N)]; Gt = [[] for _ in range(2*N)]; T, V, S = [], [0]*2*N, 1
for (a, p), (b, q) in CNF: G[a+N*(1-p)].append(b+N*q); G[b+N*(1-q)].append(a+N*p)
for i in range(2*N):
    for j in G[i]: Gt[j].append(i)
def DFS(s, t):
    U = [2*s]; a = G if t else Gt
    while U:
        ub = U.pop()
        u, b = ub//2, ub%2
        if b and t: T.append(u)
        elif V[u] == 0:
            V[u] = S; U.append(2*u+1)
            for v in a[u]:
                if V[v] == 0: U.append(2*v)
    return 1
for i in range(2*N):
    if V[i] == 0: DFS(i, 1)
V = [0]*2*N
for i in T[::-1]:
    if V[i] == 0: S += DFS(i, 0)

# Check if there is such assignment
print(not any(V[i]==V[i+N] for i in range(N)))

# Find such assignment
print([V[i]>V[i+N] for i in range(N)])