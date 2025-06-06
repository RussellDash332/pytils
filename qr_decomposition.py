def mul(A, B):
    C = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])): C[i][j] += A[i][k]*B[k][j]
    return C
def dot(u, v):
    return sum(x*y for x, y in zip(u, v))
def sub(a, b):
    return [x-y for x, y in zip(a, b)]
def normalize(a):
    n = dot(a, a)**0.5; return [x/n for x in a]
def transpose(A):
    return [*map(list, zip(*A))]

# QR decomposition resolves the issue when A^T A is singular, since the usual A^T Ax = A^T b approach won't work
def QR(A):
    aT = transpose(A); E = [normalize(aT[0])]
    for i in range(1, len(aT)):
        u = aT[i]
        for j in range(i): k = dot(E[j], u); u = sub(u, [k*x for x in E[j]])
        E.append(normalize(u))
    for i in range(len(aT), len(A)):
        u = [1]*len(aT[0])
        for j in range(len(aT)): k = dot(E[j], u); u = sub(u, [k*x for x in E[j]])
        E.append(normalize(u))
    return transpose(E), mul(E, A)

if __name__ == '__main__':
    from pprint import *
    def pmat(A):
        Z = [[round(A[i][j], 5) for j in range(len(A[0]))] for i in range(len(A))]
        pprint(Z)
    Q, R = QR(A:=[[1, 2], [3, 4]])
    print('Original matrix A:'); pmat(A); print('Matrix Q:'); pmat(Q); print('Matrix R:'); pmat(R); print('Check if A == QR:'); pmat(mul(Q, R)); print()
    Q, R = QR(A:=[[2, 3], [2, 4], [1, 1]])
    print('Original matrix A:'); pmat(A); print('Matrix Q:'); pmat(Q); print('Matrix R:'); pmat(R); print('Check if A == QR:'); pmat(mul(Q, R)); print()
    Q, R = QR(A:=[[1, 2, 3, 4], [5, 6, 7, 8], [0, 9, 1, 2], [0, 0, 3, 4]])
    print('Original matrix A:'); pmat(A); print('Matrix Q:'); pmat(Q); print('Matrix R:'); pmat(R); print('Check if A == QR:'); pmat(mul(Q, R)); print()