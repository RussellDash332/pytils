# https://tanujkhattar.wordpress.com/2016/01/11/dominator-tree-of-a-directed-graph/
# Takes in a 0-indexed adjacency list and the root vertex
class DT:
    def __init__(s, G, r):
        N = len(G); S = [-1]*N; U = [-1]*N; l = [-1]*N; h = [-1]*N; p = [-1]*N; R = [[] for _ in range(N)]; C = 0; A = [-1]*N; I = [-1]*N; B = [[] for _ in range(N)]; s.T = [[] for _ in range(N)]; s.D = [-1]*N; s1 = [2*r]; s2 = []; sf = []
        while s1:
            v, b = divmod(s1.pop(), 2)
            if b:
                for u in s2.pop(): p[A[u]] = A[v]
            elif A[v] == -1:
                A[v] = l[C] = S[C] = U[C] = C; h[C] = v; C += 1; tmp = []; s1.append(2*v+1)
                for u in G[v]:
                    if A[u] == -1: s1.append(2*u); tmp.append(u)
                s2.append(tmp)
        for i in range(N):
            for j in G[i]: R[A[j]].append(A[i])
        def find(v):
            sf.append(2*v); z = -1
            while U[v:=sf[-1]>>1] != v: sf.append(2*U[v]+1)
            while sf:
                v, c = divmod(sf.pop(), 2)
                if U[v] == v: z = -1 if c else v
                elif z < 0: z = v
                else: l[v] = l[U[v] if S[l[v]] > S[l[U[v]]] else v]; U[v] = z; z = z if c else l[v]
            return z
        # t == 0 -> it's the root
        for t1 in range(C-1, -1, -1):
            for t2 in R[t1]: S[t1] = min(S[t1], S[find(t2)])
            if t1: B[S[t1]].append(t1)
            for t2 in B[t1]: v = find(t2); I[t2] = S[t2] if S[v]==S[t2] else v
            if t1: U[t1] = p[t1]
        for t in range(1, C):
            if I[t] != S[t]: I[t] = I[I[t]]
        for t in range(1, C): s.D[h[t]] = h[I[t]]
        s.D[r] = r
        for v in range(N):
            if v != r: s.T[s.D[v]].append(v)

if __name__ == '__main__':
    # example graph from article
    G = [[3, 2, 1], [4], [5, 4, 1], [6, 7], [12], [8], [9], [9, 10], [11, 5], [11], [9], [0, 9], [8]]
    dt = DT(G, 0)
    assert dt.T == [[1, 2, 3, 4, 5, 8, 9, 11], [], [], [6, 7], [12], [], [], [10], [], [], [], [], []]
    print(dt.D) # print dominator

    # example graph from https://open.kattis.com/problems/roadblock
    G = [[1, 2], [3, 4], [3, 4], [], []]
    dt = DT(G, 0)
    assert dt.T == [[1, 2, 3, 4], [], [], [], []]
    print(dt.D) # print dominator