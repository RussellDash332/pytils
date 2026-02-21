class SqrtTree:
    def __init__(s, a, op):
        s.n = n = len(a); s.op = op; s.lg = lg = (n-1).bit_length(); s.v = v = [*a]; s.z = z = [0]*(1<<lg); s.O = O = [0]*(lg+1); s.Y = Y = []; tmp = lg
        for i in range(1, len(z)): z[i] = z[i>>1]+1
        while tmp > 1: O[tmp] = len(Y); Y.append(tmp); tmp = (tmp+1)>>1
        for i in range(lg-1, -1, -1): O[i] = max(O[i], O[i+1])
        L = (lg+1)>>1; B = 1<<L; s.iz = iz = (n+B-1)>>L; v.extend([0]*iz); s.pr = pr = [[0]*(n+iz) for _ in Y]; s.su = su = [[0]*(n+iz) for _ in Y]; s.bw = bw = [[0]*((1<<lg)+B) for _ in range(max(0, len(Y)-1))]; S = [(0, 0, n, 0)]
        while S:
            ly, lb, rb, of = S.pop()
            if ly >= len(Y): continue
            for l in range(lb, rb, B:=1<<((Y[ly]+1)>>1)):
                r = min(l+B, rb); pr[ly][l] = v[l]; su[ly][r-1] = v[r-1]
                for i in range(l+1, r): pr[ly][i] = op(pr[ly][i-1], v[i])
                for i in range(r-2, l-1, -1): su[ly][i] = op(su[ly][i+1], v[i])
                S.append((ly+1, l, r, of))
            if ly == 0:
                L = (lg+1)>>1
                for i in range(iz): v[n+i] = su[0][i<<L]
                S.append((1, n, n+iz, (1<<lg)-n))
            else:
                L = (Y[ly]+1)>>1; C = Y[ly]>>1; B = 1<<L; D = (rb-lb+B-1)>>L
                for i in range(D):
                    Z = None
                    for j in range(i, D): T = su[ly][lb+(j<<L)]; Z = op(Z, T) if i-j else T; bw[ly-1][of+lb+(i<<C)+j] = Z
    def query(s, l, r):
        S = [(l, r, 0, 0)]; T = []
        while S:
            v = S.pop()
            if v:
                l, r, of, b = v
                if l == r: T.append(s.v[l]); continue
                if l+1 == r: T.append(s.op(s.v[l], s.v[r])); continue
                ly = s.O[s.z[(l-b)^(r-b)]]; L = (s.Y[ly]+1)>>1; C = s.Y[ly]>>1; lb = ((l-b)>>s.Y[ly]<<s.Y[ly])+b; lB = ((l-lb)>>L)+1; rB = ((r-lb)>>L)-1; Z = s.op(s.su[ly][l], s.pr[ly][r])
                if lB <= rB:
                    if ly: Z = s.op(Z, s.bw[ly-1][of+lb+(lB<<C)+rB])
                    else: S.append(0); S.append((s.n+lB, s.n+rB, (1<<s.lg)-s.n, s.n))
                T.append(Z)
            else: T.append(s.op(T.pop(), T.pop()))
        return T[0]
    def update(s, idx, x):
        s.v[idx] = x; S = [(0, 0, s.n, 0, idx)]
        while S:
            ly, lb, rb, of, x = S.pop()
            if ly >= len(s.Y): continue
            L = (s.Y[ly]+1)>>1; B = 1<<L; X = (x-lb)>>L; l = lb+(X<<L); r = min(l+B, rb)
            s.pr[ly][l] = s.v[l]; s.su[ly][r-1] = s.v[r-1]
            for i in range(l+1, r): s.pr[ly][i] = s.op(s.pr[ly][i-1], s.v[i])
            for i in range(r-2, l-1, -1): s.su[ly][i] = s.op(s.su[ly][i+1], s.v[i])
            if ly == 0: s.v[s.n+X] = s.su[0][X<<((s.lg+1)>>1)]; S.append((1, s.n, s.n+s.iz, (1<<s.lg)-s.n, s.n+X))
            else:
                L = (s.Y[ly]+1)>>1; C = s.Y[ly]>>1; B = 1<<L; D = (rb-lb+B-1)>>L
                for i in range(D):
                    Z = None
                    for j in range(i, D): T = s.su[ly][lb+(j<<L)]; Z = s.op(Z, T) if i-j else T; s.bw[ly-1][of+lb+(i<<C)+j] = Z
            S.append((ly+1, l, r, of, x))

if __name__ == '__main__':
    from functools import *
    from random import *
    from math import *

    A = [564, 7167, -4069, -3244, 579, 199, -9838, 2913, 9796, 4734]

    N = len(A)
    def test(f):
        B = [*A]; S = SqrtTree(B, f:=lambda a,b:a+b)
        for i in range(N):
            for j in range(i, N):
                assert reduce(f, B[i:j+1]) == S.query(i, j), (reduce(f, B[i:j+1]), S.query(i, j), B[i:j+1])
        for _ in range(1000):
            idx = randint(0, N-1); v = randint(-10**4, 10**4)
            B[idx] = v; S.update(idx, v)
            for i in range(N):
                for j in range(i, N):
                    assert reduce(f, B[i:j+1]) == S.query(i, j), (reduce(f, B[i:j+1]), S.query(i, j), B[i:j+1])
    test(min); test(max); test(lambda x,y: x+y); test(lambda x,y: x*y)
    test(lambda x,y: x^y); test(lambda x,y: x|y); test(lambda x,y: x&y)
    test(gcd); test(lcm)