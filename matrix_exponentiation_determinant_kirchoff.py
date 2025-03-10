# Supposedly len(b) == len(a[0])
def mul(a, b):
    c = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)): c[i][j] += a[i][k]*b[k][j]
    return c

# Supposedly len(m) == len(m[0])
def matpow(m, k):
    if k == 0: return [[int(i==j) for j in range(len(m))] for i in range(len(m))]
    if k%2: return mul(matpow(m, k-1), m)
    return matpow(mul(m, m), k//2)

# len(a) == len(a[0])
eps = 1e-9
def det(a):
    z = 1; n = len(a)
    for i in range(n):
        k = i
        for j in range(i+1, n):
            if abs(a[j][i]) > abs(a[k][i]): k = j
        if abs(a[k][i]) < eps: z = 0; break
        a[i], a[k] = a[k], a[i]
        if i != k: z = -z
        z *= a[i][i]
        for j in range(i+1, n): a[i][j] /= a[i][i]
        for j in range(n):
            if j != i and abs(a[j][i]) > eps:
                for k in range(i+1, n): a[j][k] -= a[i][k]*a[j][i]
    return z

# Kirchoff's matrix tree theorem
# g is a list of lists/sets representing the adjacency list
def st(g):
    n = len(g); A = [[0]*n for _ in range(n)]
    for i in range(n):
        A[i][i] = len(g[i])
        for j in g[i]: A[i][j] -= 1
    return round(det([r[1:] for r in A[1:]]))

if __name__ == '__main__':
    fib = [[0, 1], [1, 1]]
    for n in range(10): print(matpow(fib, n))
    print(matpow(fib, 200))

    print(st([[1, 2], [0, 2, 3, 4], [0, 1, 4, 5], [1, 4, 6, 7], [1, 2, 3, 5, 7, 8], [2, 4, 8, 9], [3, 7], [3, 4, 6, 8], [4, 5, 7, 9], [5, 8]]))
    print(st([[4, 5, 6], [4, 6, 7], [5, 6, 8], [6, 7, 8], [0, 1], [0, 2], [0, 1, 2, 3], [1, 3], [2, 3]]))
    print(st([{*range(50)}-{i} for i in range(50)]))
    # 50**48?
    # Handling precision issue: use inverse modulo some large prime number