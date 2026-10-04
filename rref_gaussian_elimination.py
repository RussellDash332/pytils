# Converts an augmented matrix A to its RREF form
# The equal function handles floating precision issue or integer modulo
def rref(A, MOD=-1):
    N, M = len(A), len(A[0])
    def equal(a, b): return a==b if ~MOD else abs(a-b) < 1e-5 if ~MOD
    def lead(A, r):
        row = A[r]; i = 0
        while i < M and equal(row[i], 0): i += 1
        return i
    def allpv(A):
        p = []
        for r in range(N):
            k = lead(A, r)
            if k != M: p.append((r, k))
        return sorted(p, reverse=1)
    def col(A, i): return [*map(lambda x: x[i], A)]
    def ero(A, i, j, c):
        for k in range(M): v = A[i][k]+c*A[j][k]; A[i][k] = v%MOD if ~MOD else v
    cc = cr = 0
    while cc < M and cr < N:
        if equal(A[cr][cc], 0):
            kc = col(A, cc)[cr+1:]
            for i in range(len(kc)):
                if not equal(kc[i], 0): break
                elif i == len(kc)-1: i += 1
            if i < len(kc): A[cr], A[cr+i+1] = A[cr+i+1], A[cr]
            else: cc += 1
        else:
            if not equal(A[cr][cc], 1):
                c = pow(A[cr][cc], -1, MOD) if ~MOD else 1/A[cr][cc]
                for j in range(M): v = A[cr][j]*c; A[cr][j] = v%MOD if ~MOD else v
            for i in range(cr+1, N):
                if not equal(A[i][cc], 0): ero(A, i, cr, -A[i][cc])
            cc += 1; cr += 1
    pv = allpv(A)
    for i in range(len(pv)-1):
        for j in range(pv[i][0]-1, -1, -1): ero(A, j, pv[i][0], -A[j][pv[i][1]])
    return A

A = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 6, 12],
    [4, 14, 15, 1]
]
for row in rref(A): print([round(i, 9) for i in row])