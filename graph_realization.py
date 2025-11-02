# Takes in a degree sequence D, returns an edge list E with degree sequence D
# If the graph is *possibly* connected, E is *guaranteed* to represent a connected graph
def havel_hakimi(D):
    E = []; Q = [[] for _ in range(max(D)+1)]; L = 1; R = len(Q)-1; T = []; J = [i-1 for i in range(R+1)]
    for i in range(len(D)): Q[D[i]].append(i)
    while L <= R:
        if not Q[L]: L += 1; continue
        #while not Q[R]: R = J[R]
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

# Takes in an outdegree sequence O and an indegree sequence I, returns an edge list E with the given degree sequences
# The list O and I will get modified during the process, so copy the list if needed after
from heapq import *
def kleitman_wang(O, I):
    E = []; R = max(O+I); L = 1; P = [[] for _ in range(R+1)]; Q = [[] for _ in range(R+1)]; T = []; J = [i-1 for i in range(R+1)]
    for i in range(len(O)): P[O[i]].append((-I[i], i)); Q[I[i]].append((-O[i], i))
    for i in range(R+1): heapify(P[i]); heapify(Q[i])
    while L <= R:
        if not P[L] and not Q[L]: L += 1; continue
        #while not P[R] and not Q[R]: R = J[R]
        if (sw:=not P[L]): P, Q, O, I = Q, P, I, O
        _, v = heappop(P[L]); S = R; B = []; t = 0
        for _ in range(L):
            while S and (not Q[S] or (len(Q[S]) == 1 and Q[S][0][1] == v)): B.append(S); S = J[S]
            if S < 1: return
            _, u = heappop(Q[S])
            if u == v: _, u = heappop(Q[S]); t = S
            E.append((u, v) if sw else (v, u)); O[v] -= 1; I[u] -= 1
            if S > 1: T.append((u, S-1))
        if t: heappush(Q[t], (-O[v], v))
        while T:
            u, x = T.pop()
            if J[x+1] != x: J[x], J[x+1] = J[x+1], x
            heappush(Q[x], (-O[u], u))
        for b in B:
            if not P[J[b]] and not Q[J[b]]: J[b] = J[J[b]]
        L -= S==L
        if sw: P, Q, O, I = Q, P, I, O
    return E

if __name__ == '__main__':
    from time import *

    def validate_hh(D, show_el=True):
        T = time(); E = havel_hakimi(D)
        if show_el and E == None: return print('[hh]', None)
        X = [0]*len(D)
        for a, b in E: X[a] += 1; X[b] += 1
        assert X == D
        if show_el: print('[hh]', E)
        else: print('[hh] Done in', round(time()-T, 3), 'seconds')

    def validate_kw(O, I, show_el=True):
        assert len(O) == len(I)
        O2 = [*O]; I2 = [*I]
        T = time(); E = kleitman_wang(O2, I2)
        if show_el and E == None: return print('[kw]', None)
        X = [0]*len(O); Y = [0]*len(I)
        for a, b in E: X[a] += 1; Y[b] += 1
        if show_el: print('[kw]', E)
        else: print('[kw] Done in', round(time()-T, 3), 'seconds')

    # Test for small graphs
    validate_hh([0])
    validate_hh([1])
    validate_hh([0, 0])
    validate_hh([1, 0])
    validate_hh([1, 1])
    validate_hh([1, 3, 2, 2, 1, 3])
    validate_hh([2]*20)

    validate_kw([0], [0])
    validate_kw([1], [0])
    validate_kw([0], [1])
    validate_kw([1], [1])
    validate_kw([1, 0], [0, 1])
    validate_kw([2, 1, 2, 1, 3], [0, 2, 2, 3, 2])
    validate_kw([3]*7, [3]*7)
    validate_kw([2, 2, 1], [1, 2, 2])
    validate_kw([2, 2, 1], [1, 1, 2])

    # Examples from https://d3gt.com/unit.html?havel-hakimi
    validate_hh([4, 3, 3, 2, 2])
    validate_hh([5]*6)
    validate_hh([5, 4, 4, 5, 2, 3, 1])
    validate_hh([6, 3, 3, 5, 2, 3, 2])
    validate_hh([8, 7, 6, 5, 4, 3, 7, 8, 5, 3, 1, 5])
    validate_hh([8, 5, 4, 7, 8, 6, 6, 5, 4, 7, 8])

    # Random big graph?
    from random import *
    n = randint(1000, 3000)
    m = randint(0, n*(n-1)//2)
    print(f'Random graph with {n} vertices and {m} edges')
    graph = [set() for _ in range(n)]
    deg = [0]*n; indeg = [0]*n; outdeg = [0]*n
    for _ in range(m):
        while (a:=randint(0, n-1)) == (b:=randint(0, n-1)) or b in graph[a]: continue
        graph[a].add(b); graph[b].add(a); deg[a] += 1; deg[b] += 1; outdeg[a] += 1; indeg[b] += 1
    validate_hh(deg, False)
    validate_kw(outdeg, indeg, False)

    # Another random big graph?
    from random import *
    n = randint(5*10**4, 10**5)
    m = randint(8*10**4, 3*10**6)
    print(f'Random graph with {n} vertices and {m} edges')
    graph = [set() for _ in range(n)]
    deg = [0]*n; indeg = [0]*n; outdeg = [0]*n
    for _ in range(m):
        while (a:=randint(0, n-1)) == (b:=randint(0, n-1)) or b in graph[a]: continue
        graph[a].add(b); graph[b].add(a); deg[a] += 1; deg[b] += 1; outdeg[a] += 1; indeg[b] += 1
    validate_hh(deg, False)
    validate_kw(outdeg, indeg, False)