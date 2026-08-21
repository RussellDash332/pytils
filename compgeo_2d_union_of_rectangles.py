# Suppose R is a list of rectangles represented by the corner vertices (x1, y1) and (x2, y2)
def union_of_rectangles_area(R):
    X = set(); Q = []; T = 1; Z = 0
    for l, d, r, u in R: X.add(l); X.add(r); Q.append((u, -1, l, r)); Q.append((d, 1, l, r))
    i2x = sorted(X); P = i2x[0]-1; x2i = {x: i for i, x in enumerate(i2x)}; L = [i2x[i+1]-i2x[i] for i in range(len(i2x)-1)]
    while T < len(L): T *= 2
    C = [0]*2*T; S = [0]*2*T; W = [0]*2*T
    for i in range(len(L)): W[T+i] = L[i]
    for p in range(T-1, 0, -1): W[p] = W[2*p]+W[2*p+1]
    for y, v, x1, x2 in sorted((y, v, x2i[x1], x2i[x2]) for y, v, x1, x2 in Q):
        Z += (y-P)*S[1]; P = y; l = x1+T; r = x2+T; l0 = l; r0 = r
        while l < r:
            if l&1: C[l] += v; S[l] = W[l] if C[l] else S[2*l]+S[2*l+1] if l < T else 0; l += 1
            if r&1: r -= 1; C[r] += v; S[r] = W[r] if C[r] else S[2*r]+S[2*r+1] if r < T else 0
            l >>= 1; r >>= 1
        l0 >>= 1; r0 >>= 1
        while l0:
            S[l0] = W[l0] if C[l0] else S[2*l0]+S[2*l0+1]
            if l0 != r0: S[r0] = W[r0] if C[r0] else S[2*r0]+S[2*r0+1]
            l0 >>= 1; r0 >>= 1
    return Z

# Show the list of rectangles instead
def union_of_rectangles(R):
    X = set(); Q = []; T = 1; Z = []
    for l, d, r, u in R: X.add(l); X.add(r); Q.append((u, -1, l, r)); Q.append((d, 1, l, r))
    i2x = sorted(X); P = i2x[0]-1; x2i = {x: i for i, x in enumerate(i2x)}; L = [i2x[i+1]-i2x[i] for i in range(len(i2x)-1)]
    while T < len(L): T *= 2
    C = [0]*2*T; S = [0]*2*T; W = [0]*2*T; A = {}; Q.sort()
    for i in range(len(L)): W[T+i] = L[i]
    for p in range(T-1, 0, -1): W[p] = W[2*p]+W[2*p+1]
    i = 0; P = Q[0][0]
    while i < len(Q):
        y = Q[i][0]
        while i < len(Q) and Q[i][0] == y:
            _, v, x1, x2 = Q[i]
            D = x2i[x1]; E = x2i[x2]; U = [(1, 0, T, 0)]
            while U:
                p, s, l, b = U.pop()
                if b:
                    if C[p]:    S[p] = W[p]
                    elif p < T: S[p] = S[2*p]+S[2*p+1]
                    else:       S[p] = 0
                else:
                    U.append((p, s, l, 1))
                    if D <= s <= E-l: C[p] += v
                    else:
                        if E > s > D-l//2: U.append((2*p, s, l//2, 0))
                        if E+l//2 > s+l > D: U.append((2*p+1, s+l//2, l//2, 0))
            i += 1
        K = []; U = [(1, 0, T)]
        while U:
            p, s, l = U.pop()
            if C[p]: K.append((i2x[s], i2x[min(s+l, len(i2x)-1)]))
            elif p < T: U.append((2*p, s, l//2)); U.append((2*p+1, s+l//2, l//2))
        B = set(K)
        for x in A.keys()-B: Z.append((x[0], A[x], x[1], y)); del A[x]
        for x in B-A.keys(): A[x] = y
        P = y
    for x, y0 in A.items(): Z.append((x[0], y0, x[1], P))
    return Z

if __name__ == '__main__':
    U = union_of_rectangles(T:=[
        (0, 0, 2, 3),
        (3, 4, 5, 7),
        (1, 2, 4, 5)
    ])
    print(U)
    assert union_of_rectangles_area(T) == sum((x2-x1)*(y2-y1) for x1, y1, x2, y2 in U)

    U = union_of_rectangles(T:=[
        (0, 0, 2, 3),
        (3, 4, 5, 7),
        (2, 3, 3, 4)
    ]) # also works if they are all disjoint
    print(U)
    assert union_of_rectangles_area(T) == sum((x2-x1)*(y2-y1) for x1, y1, x2, y2 in U)