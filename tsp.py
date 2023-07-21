from itertools import combinations
INF = 1e18
def tsp(G):
    n = len(G); C = [[INF for _ in range(n)] for _ in range(1<<n)]; C[1][0] = 0
    for s in range(1, n):
        for S in combinations(range(1, n), s):
            k = 1
            for i in S: k += 1<<i
            for i in S:
                C[k][i] = min(C[k][i], C[k^(1<<i)][0]+G[0][i])
                for j in S:
                    if j != i: C[k][i] = min(C[k][i], C[k^(1<<i)][j]+G[j][i])
    k = (1<<n)-1; return min((C[k][i]+G[i][0], i) for i in range(n))

INF = 1e18
def tsp2(G):
    n = len(G); C = [[INF for _ in range(n)] for _ in range(1<<n)]; C[1][0] = 0
    p = [[0 for _ in range(n)] for _ in range(1<<n)]
    for s in range(1<<n):
        for i in range(n):
            for j in range(n):
                if s&(1<<j) == 0: s2 = s+(1<<j); C[s2][j], p[s2][j] = min((C[s][i]+G[i][j], i), (C[s2][j], p[s2][j]))
    tour = [n-1]; pos = n-1; k = (1<<n)-1
    while pos: nxt = p[k][pos]; k -= 1<<pos; pos = nxt; tour.append(pos)
    return tour[::-1]

G = [
    [0, 20, 42, 35],
    [20, 0, 30, 34],
    [42, 30, 0, 12],
    [35, 34, 12, 0]
]
G2 = [[0]]
G3 = [
    [0, 1, 55],
    [1, 0, 3],
    [55, 3, 0]
]

# more useful to find the cost
print(tsp(G))
print(tsp(G2))
print(tsp(G3))

# better to enumerate tours
print(tsp2(G))
print(tsp2(G2))
print(tsp2(G3))