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