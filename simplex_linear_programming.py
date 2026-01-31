# n = number of variables, m = number of constraints
# all constraints still subject to x_i >= 0

# Credits: Brandon Tang
# Should work on general cases, especially when it includes a lower bound
INF = float('inf'); EPS = 1e-5
def simplex(A, C):
    def pivot(r, s):
        k = 1/D[r][s]
        for i in range(m+2):
            if i == r: continue
            for j in range(n+2):
                if j != s: D[i][j] -= D[r][j]*D[i][s]*k
        for i in range(n+2): D[r][i] *= k
        for i in range(m+2): D[i][s] *= -k
        D[r][s] = k; B[r], N[s] = N[s], B[r]
    def find(p):
        while True:
            if D[m+p][s:=min((i for i in range(n+1) if p or N[i] != -1), key=lambda x: (D[m+p][x], N[x]))] > -EPS: return 1
            if (r:=min((i for i in range(m) if D[i][s] > EPS), key=lambda x: (D[x][-1]/D[x][s], B[x]), default=-1)) == -1: return 0
            pivot(r, s)
    m = len(A); n = len(A[0])-1; N = [*range(n), -1]; B = [*range(n, n+m)]; D = [*([*A[i], -1] for i in range(m)), C+[0]*2, [0]*(n+2)]
    for i in range(m): D[i][-2], D[i][-1] = D[i][-1], D[i][-2]
    D[-1][n] = 1; r = min(range(m), key=lambda x: D[x][-1])
    if D[r][-1] < -EPS and (pivot(r, n) or not find(1) or D[-1][-1] < -EPS): return -INF, None
    for i in range(m): B[i] == -1 and pivot(i, min(range(n), key=lambda x: (D[i][x], N[x])))
    if find(0):
        x = [0]*n
        for i in range(m):
            if 0 <= B[i] < n: x[B[i]] = D[i][-1]
        return sum(C[i]*x[i] for i in range(n)), x # or -D[m][-1]
    else: return -INF, None

# Old version (might be faster), but only works on positive A-entries
def simplex_old(A, C):
    m, n = len(A), len(A[0])-1; c = [[0]*(m+n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n): c[i][j] = A[i][j]
        c[i][-1] = A[i][-1]
    for i in range(n): c[-1][i] = C[i]
    for i in range(m): c[i][i+n] = 1
    while True:
        if (col:=min([(i,e) for i,e in enumerate(c[-1]) if e<0], key=lambda x: x[1], default=[-1])[0]) == -1: break
        if (row:=min([(i,e,c[i][-1]/c[i][col]) for i,e in enumerate(c[t][col] for t in range(m)) if e>0], key=lambda x: x[2], default=[-1])[0]) == -1: break
        k = c[row][col]
        for i in range(m+n+1): c[row][i] /= k
        for i in range(m+1):
            if i == row: continue
            k = c[i][col]
            for j in range(m+n+1): c[i][j] -= k*c[row][j]
    return -c[-1][-1]

A = [
    [0.5, 0, 100],      # 0.5x <= 100
    [0.5, 0.5, 150],    # 0.5x + 0.5y <= 150
    [0, 0.5, 100]       # 0.5y <= 100
]
C = [-3.2, -2.8]        # minimize -3.2x - 2.8y <-> maximize 3.2x + 2.8y
print(simplex(A, C))    # optimal when x = 200, y = 100
print(simplex_old(A, C))

# Another example
A = [
    [1, 2, 2, 1, 1, 0, 12],     # x1 + 2x2 + 2x3 + x4 + x5 <= 12
    [1, 2, 1, 1, 2, 1, 18],     # x1 + 2x2 + x3 + x4 + 2x5 + x6 <= 18
    [3, 6, 2, 1, 3, 0, 24]      # 3x1 + 6x2 + 2x3 + x4 + 3x5 <= 24
]
C = [-1, 2, 3, 1, 1, -2]        # minimize -x1 + 2x2 + 3x3 + x4 + x5 - 2x6
print(simplex(A, C))
print(simplex_old(A, C))

# How about bounded on both sides?
A = [
    [-1, 0, -1],
    [1, 0, 3],      # 1 <= x <= 3
    [0, -1, -2],
    [0, 1, 5]       # 2 <= y <= 5
]
C = [50, 40]        # can tell that 50x + 40y >= 130
print(simplex(A, C))

# Equality?
A = [
    [-1, 0, -1],    # x = 1
    [1, 0, 1],
    [0, -1, -4],    # y = 4
    [0, 1, 4]
]
C = [500, -40]      # 500x - 40y = 340
print(simplex(A, C))

# Infinity?
A = [
    [-1, -4, -3],   # x + 4y >= 3
    [-2, -1, -5]    # 2x + y >= 5
]
C = [-1, 2]         # minimize -x + 2y <-> maximize x - 2y
print(simplex(A, C))