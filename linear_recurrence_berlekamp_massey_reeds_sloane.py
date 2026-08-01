# This is O(N^2) because the O(N log N) approach, when implemented, has a large constant factor
def berlekamp_massey(S, M=998244353):
    C = [1]; B = [1]; L = 0; m = b = 1
    for n, s in enumerate(S):
        if (d:=(s+sum(C[i]*S[n-i] for i in range(1, L+1)))%M):
            T = C[:]; c = d*pow(b, -1, M)%M; C.extend([0]*(len(B)+m-len(C)))
            for i in range(len(B)): C[i+m] = (C[i+m]-c*B[i])%M
            if 2*L > n: m += 1
            else: L = n+1-L; B = T; b = d; m = 1
        else: m += 1
    return [-x%M for x in C[1:]]

print(berlekamp_massey([1, 1, 2, 3, 5, 8, 13, 21, 34, 55]))
print(berlekamp_massey([1, 13, 948, 12, 4, 23, 7, 67, 67], 10**9+7)) # different modulo

# ---

from math import prod
from subprocess import *
from collections import *
def reeds_sloane(S, p, e):
    M = p**e; C = [1]; L = 0; B = [[1] for _ in range(e)]; b = [1]*e; l = [0]*e; m = [1]*e
    for n, s in enumerate(S):
        if (d:=(s+sum(C[i]*S[n-i] for i in range(1, L+1)))%M):
            k, c = 0, d
            while c%p<1: c //= p; k += 1
            c %= M; r = max(range(k+1), key=lambda i: (n+1-l[i], i)); T = C[:]; c2 = (c*pow(b[r], -1, M)*pow(p, k-r, M))%M; C.extend([0]*(len(B[r])+m[r]-len(C)))
            for i in range(len(B[r])): C[i+m[r]] = (C[i+m[r]]-c2*B[r][i])%M
            for j in range(e): m[j] += 1
            if n+1-l[r] > L: L = n+1-l[r]; B[k], b[k], l[k], m[k] = T, c, L, 1
        else:
            for j in range(e): m[j] += 1
    return [-x%M for x in C[1:]]
def berlekamp_massey(S, M=998244353):
    pf = Counter(map(int, check_output(f"factor {M}",shell=1).split()[1:])); pe = [p**e for p,e in pf.items()]; L = max(map(len, P:=[reeds_sloane(S, p, e) for p, e in pf.items()]))
    for z in P: z.extend([0]*(L-len(z)))
    return [sum(r*pow(n:=M//m, -1, m)*n for r, m in zip(q, pe))%M for q in zip(*P)]

print(berlekamp_massey([1, 1, 2, 3, 5, 8, 13, 21, 34, 55]))
print(berlekamp_massey([1, 1, 2, 3, 12, 8, 12, 21, 34, 55], 2))
print(berlekamp_massey([1, 13, 948, 12, 4, 23, 7, 67, 67], 10**9+7))    # different modulo
print(berlekamp_massey([1, 5, 3, 7, 11, 1, 9, 5], 12))                  # non-prime modulo
print(berlekamp_massey([1, 13, 948, 12, 4, 23, 7, 67, 67], 100))        # non-prime modulo