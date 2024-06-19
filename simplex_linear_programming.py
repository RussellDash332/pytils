# n = number of variables, m = number of constraints
# all constraints still subject to x_i >= 0

# Credits: Brandon Tang
# Should work on general cases, especially when it includes a lower bound
INF = float('inf'); EPS = 1e-5
def simplex(A, C):
    m = len(A); n = len(A[0])-1; D = [[0]*(n+2) for _ in range(m+2)]; N = [0]*(n+1); B = [0]*m
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
            s = r = -1
            for i in range(n+1):
                if (p or N[i] != -1) and (s == -1 or (D[m+p][i], N[i]) < (D[m+p][s], N[s])): s = i
            if D[m+p][s] > -EPS: return 1
            for i in range(m):
                if D[i][s] > EPS and (r == -1 or (D[i][-1]/D[i][s], B[i]) < (D[r][-1]/D[r][s], B[r])): r = i
            if r == -1: return 0
            pivot(r, s)
    for i in range(m):
        for j in range(n): D[i][j] = A[i][j]
        B[i] = n+i; D[i][n] = -1; D[i][-1] = A[i][-1]
    for i in range(n): N[i] = i; D[m][i] = C[i]
    N[n] = -1; D[-1][n] = 1; r = min(range(m), key=lambda x: D[x][-1])
    if D[r][-1] < -EPS:
        pivot(r, n)
        if not find(1) or D[-1][-1] < -EPS: return -INF
    for i in range(m):
        if B[i] != -1: continue
        s = -1
        for j in range(n):
            if s == -1 or D[i][j] < D[i][s] or (D[i][j] == D[i][s] and N[j] < N[s]): s = j
        pivot(i, s)
    return -D[m][-1] if find(0) else INF

# Definitely shorter (might be faster), but only works on positive A-entries
def simplex_positive(A, C):
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
C = [-3.2, -2.8]        # minimize -3.2x-2.8y <-> maximize 3.2x+2.8y
print(simplex(A, C))    # optimal when x = 200, y = 100
print(simplex_positive(A, C))

# Another one that you can try
A = [
    [1, 2, 2, 1, 1, 0, 12],     # x1 + 2x2 + 2x3 + x4 + x5 <= 12
    [1, 2, 1, 1, 2, 1, 18],     # x1 + 2x2 + x3 + x4 + 2x5 + x6 <= 18
    [3, 6, 2, 1, 3, 0, 24]      # 3x1 + 6x2 + 2x3 + x4 + 3x5 <= 24
]
C = [-1, 2, 3, 1, 1, -2]        # minimize -x1 + 2x2 + 3x3 + x4 + x5 - 2x6
print(simplex(A, C))
print(simplex_positive(A, C))

# How about bounded on both sides?
A = [
    [-1, 0, -1],
    [1, 0, 3],      # 1 <= x <= 3
    [0, -1, -2],
    [0, 1, 5]       # 2 <= y <= 5
]
C = [50, 40]        # can tell that 50x + 40y >= 130
print(simplex(A, C))
#print(simplex_positive(A, C))

# Equality?
A = [
    [-1, 0, -1],    # x = 1
    [1, 0, 1],
    [0, -1, -4],    # y = 4
    [0, 1, 4]
]
C = [500, -40]
print(simplex(A, C))
#print(simplex_positive(A, C))