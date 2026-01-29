_OLD_POW = pow

# String representation of polynomial
def rep(p):
    n = len(p); sb = []
    for i in range(n):
        if p[i] not in [-1, 1]: sb.append(str(p[i]))
        elif p[i] == -1: sb.append('-')
        if i > 0: sb.append(f'x^{i}')
        if i < n-1 and p[i+1] > 0: sb.append('+')
    return ''.join(sb).replace('^1','')

################################
# Fast Fourier transform (FFT) #
################################

# FFT, handles both FFT and IFFT
# n should be a power of 2
# Note, if prone to floating point error, recompute wj instead of multiplying by w every time
from math import *
def fft(v, inv=False):
    n = len(v)
    if n == 1: return v
    ye, yo = fft(v[::2], inv), fft(v[1::2], inv); y, a, wj = [0]*n, (2-4*inv)*pi/n, 1; w = complex(cos(a), sin(a))
    for i in range(n//2): y[i] = ye[i]+wj*yo[i]; y[i+n//2] = ye[i]-wj*yo[i]; wj *= w
    return y

# Iterative version, better approach for https://open.kattis.com/problems/polymul2
from cmath import *
def fft(v, inv=False):
    stack = [(2*len(v), v)]; tmp = []
    while stack:
        nb, v = stack.pop(); n, b = nb//2, nb%2
        if b == 0:
            if n == 1: tmp.append(v)
            else: stack.append((2*n+1, v)), stack.append((n, v[1::2])), stack.append((n, v[::2]))
        else:
            yo, ye = tmp.pop(), tmp.pop(); y, wj = [0]*n, 1; w = exp(-1j*(2-4*inv)*pi/n)
            for i in range(n//2): y[i] = ye[i]+wj*yo[i]; y[i+n//2] = ye[i]-wj*yo[i]; wj *= w
            tmp.append(y)
    return tmp[0]

# Iterative version, better approach for https://open.kattis.com/problems/polymul1
from cmath import *
def fft(v, inv=False):
    n = len(v); j = 0; k = 2
    for i in range(1, n):
        b = n>>1
        while j&b: j ^= b; b >>= 1
        j ^= b
        if i < j: v[i], v[j] = v[j], v[i]
    wk = exp(1j*(1-2*inv)*pi)
    while k <= n:
        for i in range(0, n, k):
            w = 1
            for j in range(i, i+(k>>1)): y = v[j+(k>>1)]*w; v[j+(k>>1)] = v[j]-y; v[j] += y; w *= wk
        k <<= 1; wk **= .5
    return v

# Multiply two polynomials
# x^2 + 3x + 7 -> [7, 3, 1]
def mult(p1, p2):
    n = 2**(len(bin(m:=len(p1)+len(p2)-1))-2); fft1, fft2 = fft(p1+[0]*(n-len(p1))), fft(p2+[0]*(n-len(p2)))
    return [t.real/n for t in fft([fft1[i]*fft2[i] for i in range(n)], inv=True)][:m]

####################################
# Number theoretic transform (NTT) #
####################################

BIG_M = 39582418599937 # but the primitive root is 5
BIG_M = 79164837199873 # but the primitive root is 5
BIG_M = 9223372036737335297
BIG_M = 2524775926340780033

# https://judge.yosupo.jp/submission/149376
pow = _OLD_POW
M = 998244353; R = [1, 1]
def ntt(P):
    n = len(P); L = len(bin(n))-3; Z = [0]*n; k = 1
    while len(R) < n:
        u = pow(3, M//(2*len(R)), M) # 3 is a primitive root of M
        for i in range(len(R), 2*len(R)): R.append(R[i//2]*(u if i&1 else 1)%M)
    for i in range(n): Z[i] = (Z[i//2]|(i&1)<<L)//2
    P = [P[r] for r in Z]
    while k < n:
        for i in range(0, n, 2*k):
            for j in range(k): z = R[j+k]*P[i+j+k]%M; P[i+j+k] = (P[i+j]-z)%M; P[i+j] = (P[i+j]+z)%M
        k <<= 1
    return P

# https://judge.yosupo.jp/submission/149374
pow = _OLD_POW
M = 998244353; R = [1]
def ntt(P):
    n = k = len(P); P = [*P]; Z = [0]*n
    while 2*len(R) < n: u = pow(3, M//(4*len(R)), M); R.extend([r*u%M for r in R]) # 3 is a primitive root of M
    while k > 1:
        for i in range(n//k):
            r = R[i]
            for j in range(i*k, i*k+k//2): z = r*P[j+k//2]; P[j+k//2] = (P[j]-z)%M; P[j] = (P[j]+z)%M
        k >>= 1
    for i in range(1, n): Z[i] = Z[i//2]//2+(i&1)*n//2
    return [P[r] for r in Z]

def mult(p1, p2):
    m = len(p1)+len(p2)-1; n = 1
    while n < m: n *= 2
    p1 += [0]*(n-len(p1)); p2 += [0]*(n-len(p2)); ntt1 = ntt(p1); ntt2 = ntt(p2)
    z = pow(n, -1, M); return ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)])[:m]

# Use two primes such that P*Q is sufficiently large to contain M
pow = _OLD_POW
def mult_mod(p1, p2, M=10**9+7):
    P = 39582418599937
    Q = 79164837199873
    R = pow(P, -1, Q)
    def mult(p1, p2, M):
        R = [1, 1]
        def ntt(P, M):
            n = len(P); L = len(bin(n))-3; Z = [0]*n; k = 1
            while len(R) < n:
                u = pow(5, M//(2*len(R)), M) # both P and Q have primitive root 5
                for i in range(len(R), 2*len(R)): R.append(R[i//2]*(u if i&1 else 1)%M)
            for i in range(n): Z[i] = (Z[i//2]|(i&1)<<L)//2
            P = [P[r] for r in Z]
            while k < n:
                for i in range(0, n, 2*k):
                    for j in range(k): z = R[j+k]*P[i+j+k]%M; P[i+j+k] = (P[i+j]-z)%M; P[i+j] = (P[i+j]+z)%M
                k <<= 1
            return P
        m = len(p1)+len(p2)-1; n = 1
        while n < m: n *= 2
        p1 += [0]*(n-len(p1)); p2 += [0]*(n-len(p2)); ntt1 = ntt(p1, M); ntt2 = ntt(p2, M)
        z = pow(n, -1, M); return ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)], M)[:m]
    z = [(((x:=a+(b-a)*R%Q*P)%M)-(x>P*Q//2)*P*Q)%M for a, b in zip(mult(p1, p2, P), mult(p1, p2, Q))] # CRT
    while len(p1)>1 and p1[-1] == 0: p1.pop()
    while len(p2)>1 and p2[-1] == 0: p2.pop()
    return z

#######################
# Polynomial division #
#######################

# Assume that NTT is used with modulo M and there is no remainder
# Return the quotient
pow = _OLD_POW
def div(u, v):
    b = 0
    while v[b] == 0: b += 1
    v = v[b:]; vi = [pow(v[0], -1, M)]; n = len(u)-len(v)+1; x = 1; w = []
    while x < n:
        x <<= 1
        while len(w) < min(x, len(v)): w.append(v[len(w)])
        q = mult(mult(vi, vi), w)
        while len(w) > min(x, len(v)) and w[-1] == 0: w.pop()
        while len(vi) < x: vi.append(0)
        for i in range(len(vi)):
            vi[i] <<= 1
            if i < len(q): vi[i] -= q[i]
            vi[i] %= M
    return mult(u, vi)[b:n]

# General division, possibly with remainders
# Return (quotient, remainder)
def div(P, Q):
    def sub(u, v):
        z = [*u]
        while len(z) < len(v): z.append(0)
        for i in range(len(v)): z[i] -= v[i]; z[i] %= M
        while z[-1] == 0: z.pop()
        return z
    while P and P[-1] == 0: P.pop()
    while Q and Q[-1] == 0: Q.pop()
    u = P[::-1]; v = Q[::-1]; vi = [pow(v[0], -1, M)]; n = len(u)-len(v)+1; p = 1; w = []
    while p < n:
        p *= 2
        while len(w) < min(p, len(v)): w.append(v[len(w)])
        qi = mult(mult(vi, vi), w)
        while len(w) > min(p, len(v)) and w[-1] == 0: w.pop()
        while len(vi) < p: vi.append(0)
        for i in range(len(vi)): vi[i] *= 2; vi[i] %= M
        vi = sub(vi, qi)
    z = mult(u, vi)[:n][::-1]
    return z, sub(P, mult(Q, z))

#####################
# Linear recurrence #
#####################

# Solves for a_n (mod M) given c = [c_0, c_1, ..., c_{k-1}] and a = [a_0, a_1, a_2, ..., a_{k-1}]
# The recurrence is a_i = sum(c_j * a_{i-j-1} for j in range(k))
def kitamasa(c, a, n):
    d = [1]; x = [0, 1]; f = [-i for i in c[::-1]]+[1]
    while n:
        if n%2: d = div(mult(d, x), f)[1]
        n >>= 1; x = div(mult(x, x), f)[1]
    return sum(p*q for p,q in zip(a,d))%M

if __name__ == '__main__':
    for i in range(1, 11):
        print(i, kitamasa([1, 1], [0, 1], i)) # F_i mod M
    print(kitamasa([1, 1], [2, 1], 12)) # L_12 mod M
    print(kitamasa([2, 1], [3, 5], 7), (1.5+2**-.5)*(1+2**.5)**7 + (1.5-2**-.5)*(1-2**.5)**7) # f(n) = 2*f(n-1) + f(n-2)
    print(mult_mod([1, 2, 1], [1, -2, 1], 10**9+7))
    print(mult([1, 2, 1], [1, -2, 1]))