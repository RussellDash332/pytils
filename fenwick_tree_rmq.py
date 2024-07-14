# For min update/query, change all max calls to min and update the default value
DEFAULT_VALUE = 0


# Point update, range query (PURQ)
# update:   A[i] = max(A[i], x)
# query:    max(A[i:j+1])
N = 10
A = [DEFAULT_VALUE]*2*N
def update(i, x):
    i += N; A[i] = x
    while i > 1: i >>= 1; A[i] = max(A[i<<1], A[(i<<1)+1])
def query(i, j):
    i += N; j += N; x = DEFAULT_VALUE
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = max(x, A[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = max(x, A[j-1]); j >>= 1
    return x

if __name__ == '__main__': # testing
    B = [1, 10, 8, 3, 2, 4, 5, 1, 1]
    N = len(B); A = [DEFAULT_VALUE]*2*N
    for i in range(N): update(i, B[i])
    for i in range(N):
        for j in range(i, N): assert query(i, j+1)==max(B[i:j+1])


# Range update, point query (RUPQ)
# update:   for i in range(l, r+1): A[i] = max(A[i], x)
# query:    A[i]
N = 10
A = [DEFAULT_VALUE]*2*N
def update(l, r, x):
    l += N; r += N
    while l <= r:
        if l&1: A[l] = max(A[l], x)
        if r^1&1: A[r] = max(A[r], x)
        l = (l+1)>>1; r = (r-1)>>1
def query(i):
    i += N; z = DEFAULT_VALUE
    while i > 0: z = max(z, A[i]); i >>= 1
    return z

if __name__ == '__main__': # testing
    N = 8; B = [0]*N; A = [DEFAULT_VALUE]*2*N
    I = [(3, 4, 1), (2, 5, 3), (0, 4, 7), (5, 7, 6), (1, 1, 10), (6, 6, 8), (3, 4, 12)]
    for a, b, x in I:
        for i in range(a, b+1): B[i] = max(B[i], x)
        update(a, b, x)
    for i in range(N): assert query(i)==B[i]
    print(B)