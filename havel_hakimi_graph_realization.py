# Takes in a degree sequence D, returns an edge list E with degree sequence D
# If the graph is *possibly* connected, E is *guaranteed* to represent a connected graph
def havel_hakimi(D):
    E = []; Q = [[] for _ in range(max(D)+1)]; L = 1; R = len(Q)-1; T = []; J = [i-1 for i in range(R+1)]
    for i in range(len(D)): Q[D[i]].append(i)
    while L <= R:
        if not Q[L]: L += 1; continue
        v = Q[L].pop(); S = R; B = []
        for _ in range(L):
            while S and not Q[S]: B.append(S); S = J[S]
            if S < 1: return
            u = Q[S].pop(); E.append((u, v))
            if S > 1: T.append((u, S-1))
        while T:
            u, x = T.pop()
            if J[x+1] != x: J[x], J[x+1] = J[x+1], x
            Q[x].append(u)
        for b in B:
            if not Q[J[b]]: J[b] = J[J[b]]
        L -= S==L
    return E

if __name__ == '__main__':
    def validate(D, verbose=True):
        E = havel_hakimi(D)
        if E == None: return print(None)
        X = [0]*len(D)
        for a, b in E: X[a] += 1; X[b] += 1
        assert X == D
        if verbose: print(E)

    # Test for small graphs
    validate([0])
    validate([1])
    validate([0, 0])
    validate([1, 0])
    validate([1, 1])
    validate([1, 3, 2, 2, 1, 3])
    validate([2]*20)

    # Examples from https://d3gt.com/unit.html?havel-hakimi
    validate([4, 3, 3, 2, 2])
    validate([5]*6)
    validate([5, 4, 4, 5, 2, 3, 1])
    validate([6, 3, 3, 5, 2, 3, 2])
    validate([8, 7, 6, 5, 4, 3, 7, 8, 5, 3, 1, 5])
    validate([8, 5, 4, 7, 8, 6, 6, 5, 4, 7, 8])

    # Random big graph?
    from random import *
    n = randint(1000, 3000)
    m = randint(0, n*(n-1)//2)
    print(f'Random graph with {n} vertices and {m} edges')
    graph = [set() for _ in range(n)]
    deg = [0]*n
    for _ in range(m):
        while (a:=randint(0, n-1)) == (b:=randint(0, n-1)) or b in graph[a]: continue
        graph[a].add(b); graph[b].add(a); deg[a] += 1; deg[b] += 1
    validate(deg, False)