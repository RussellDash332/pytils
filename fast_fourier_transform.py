# String representation of polynomial
def rep(p):
    n = len(p); sb = []
    for i in range(n):
        if p[i] not in [-1, 1]: sb.append(str(p[i]))
        elif p[i] == -1: sb.append('-')
        if i > 0: sb.append(f'x^{i}')
        if i < n-1 and p[i+1] > 0: sb.append('+')
    return ''.join(sb).replace('^1','')

# FFT, handles both FFT and IFFT
# n should be a power of 2
from math import *
def fft(v, inv=False):
    n = len(v)
    if n == 1: return v
    ye, yo = fft(v[::2], inv), fft(v[1::2], inv); y, a, wj = [0]*n, (2-4*inv)*pi/n, 1; w = complex(cos(a), sin(a))
    for i in range(n//2): y[i] = ye[i]+wj*yo[i]; y[i+n//2] = ye[i]-wj*yo[i]; wj *= w
    return y

# Iterative version
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

# Multiply two polynomials
# x^2 + 3x + 7 -> [7, 3, 1]
def mult(p1, p2):
    n = 2**(len(bin(m:=len(p1)+len(p2)-1))-2); fft1, fft2 = fft(p1+[0]*(n-len(p1))), fft(p2+[0]*(n-len(p2)))
    return [t.real/n for t in fft([fft1[i]*fft2[i] for i in range(n)], inv=True)][:m]