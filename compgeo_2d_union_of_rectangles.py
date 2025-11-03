# Suppose R is a list of rectangles represented by the corner vertices (x1, y1) and (x2, y2)
def union_of_rectangles(R):
    X = set(); Q = []; T = 1; Z = 0; P = min(R)[0]-1
    for x1, y1, x2, y2 in R: X.add(x1); X.add(x2); Q.append((y2, -1, x1, x2)); Q.append((y1, 1, x1, x2))
    i2x = sorted(X); x2i = {i2x[i]: i for i in range(len(i2x))}; L = [i2x[i+1]-i2x[i] for i in range(len(i2x)-1)]
    while T < len(L): T *= 2
    C = [0]*2*T; S = [0]*2*T; W = [0]*2*T
    for i in range(len(L)): W[T+i] = L[i]
    for p in range(T-1, 0, -1): W[p] = W[2*p]+W[2*p+1]
    for y, v, x1, x2 in sorted(Q):
        Z += (y-P)*S[1]; D = x2i[x1]; E = x2i[x2]; U = [(1, 0, T, 0)]; P = y
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
    return Z

if __name__ == '__main__':
    print(union_of_rectangles([
        (0, 0, 2, 3),
        (3, 4, 5, 7),
        (1, 2, 4, 5)
    ]))
    print(union_of_rectangles([
        (0, 0, 2, 3),
        (3, 4, 5, 7),
        (2, 3, 3, 4)
    ])) # also works if they are all disjoint