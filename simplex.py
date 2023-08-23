# m = number of variables, n = number of constraints
def simplex(A, C):
    n, m = len(A), len(A[0])-1
    c = [[0]*(m+n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m): c[i][j] = A[i][j]
        c[i][-1] = A[i][-1]
    for i in range(m): c[-1][i] = C[i]
    for i in range(n): c[i][i+m] = 1
    while True:
        if (col:=min([(i,e) for i,e in enumerate(c[-1]) if e<0], key=lambda x: x[1], default=[-1])[0]) == -1: break
        if (row:=min([(i,e,c[i][-1]/c[i][col]) for i,e in enumerate(c[t][col] for t in range(n)) if e>0], key=lambda x: x[2], default=[-1])[0]) == -1: break
        k = c[row][col]
        for i in range(m+n+1): c[row][i] /= k
        for i in range(n+1):
            if i == row: continue
            k = c[i][col]
            for j in range(m+n+1): c[i][j] -= k*c[row][j]
    return c[-1][-1]

A = [
    [0.5, 0, 100],      # 0.5x <= 100
    [0.5, 0.5, 150],    # 0.5x + 0.5y <= 150
    [0, 0.5, 100]       # 0.5y <= 100
]
C = [-3.2, -2.8]        # minimize -3.2x-2.8y
print(simplex(A, C))    # optimal when x = 200, y = 100

# Another one that you can try
A = [
    [1, 2, 2, 1, 1, 0, 12],     # x1 + 2x2 + 2x3 + x4 + x5 <= 12
    [1, 2, 1, 1, 2, 1, 18],     # x1 + 2x2 + x3 + x4 + 2x5 + x6 <= 18
    [3, 6, 2, 1, 3, 0, 24]      # 3x1 + 6x2 + 2x3 + x4 + 3x5 <= 24
]
C = [-1, 2, 3, 1, 1, -2]        # minimize -x1 + 2x2 + 3x3 + x4 + x5 - 2x6
print(simplex(A, C))