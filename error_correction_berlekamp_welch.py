MOD = 10**9+7
def rref(A):
    N, M = len(A), len(A[0])
    def equal(a, b): return a==b if ~MOD else abs(a-b) < 1e-5
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
def berlekamp_welch(T, Y, K, L):
    Q = len(T); mat = []
    for q in range(Q):
        tq = T[q]; yq = Y[q]; row = []; tp = 1
        for j in range(K+L): row.append(tp); tp = tp*tq%MOD
        tp = 1
        for j in range(L): row.append(-yq*tp%MOD); tp = tp*tq%MOD
        row.append(yq*tp%MOD); mat.append(row)
    rref(mat)
    if L == 0: return [mat[j][-1] for j in range(K)]
    nv = K+2*L; S = [0]*nv
    for r in range(len(mat)):
        c = 0
        while c < nv and mat[r][c] < 1: c += 1
        if c < nv: S[c] = mat[r][-1]
    # long division N/E
    Nx = S[:K+L]; np = len(Px:=Nx[:])-1; nq = len(Ex:=S[K+L:]+[1])-1; Qx = [0]*(np-nq+1)
    for i in range(np-nq, -1, -1):
        c = Px[i+nq]*pow(Ex[nq], -1, MOD)%MOD; Qx[i] = c
        for j in range(nq+1): Px[i+j] = (Px[i+j]-c*Ex[j])%MOD
    return Qx

# K = how many coefficients to discover
# L = how many lies at maximum (there might be < L errors in the data)
# This means len(T) == len(Y) >= K + 2L
if __name__ == '__main__':
    # 0 lies
    # Recovers P(t) = 2t+3 from (1, 5) and (2, 7)
    T1 = [1, 2]
    Y1 = [5, 7]
    print(berlekamp_welch(T1, Y1, 2, 0))

    # Maximum 1 lie
    # Recovers P(t) = 2t+3 with 1 lie at (2, 99)
    T2 = [1, 2, 3, 4]
    Y2 = [5, 99, 9, 11]
    print(berlekamp_welch(T2, Y2, 2, 1))

    # Maximum 2 lies
    # Recovers P(t) = 2t^2+4t+1 with 1 lie at (3, 999)
    T3 = [1, 2, 3, 4, 5, 6, 7]
    Y3 = [7, 17, 999, 49, 71, 97, 127]
    print(berlekamp_welch(T3, Y3, 3, 2))