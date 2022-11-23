from math import *

# String representation of polynomial
def rep(p):
    n = len(p)
    sb = []
    for i in range(n):
        if p[i] not in [-1, 1]:
            sb.append(str(p[i]))
        elif p[i] == -1:
            sb.append('-')
        if i > 0:
            sb.append(f'x^{i}')
        if i < n-1 and p[i+1] > 0:
            sb.append('+')
    return ''.join(sb).replace('^1','')

# FFT, handles both FFT and IFFT
# n should be a power of 2
def fft(v, inv=False):
    n = len(v)
    if n == 1:
        return v
    ye, yo = fft(v[::2], inv), fft(v[1::2], inv)
    y = [0]*n
    for i in range(n//2):
        a = (2-4*inv)*pi*i/n
        wj = complex(cos(a), sin(a))
        y[i] = ye[i] + wj * yo[i]
        y[i + n//2] = ye[i] - wj * yo[i]
    return y

# Multiply two polynomials
# x^2 + 3x + 7 -> [7, 3, 1]
def mult(p1, p2):
    m = len(p1) + len(p2) - 1
    n = 2**(len(bin(m)) - 2) # pad to next power of 2
    p1 = p1 + [0]*(n - len(p1))
    p2 = p2 + [0]*(n - len(p2))
    fft1, fft2 = fft(p1), fft(p2)
    return [t.real/n for t in fft([fft1[i]*fft2[i] for i in range(n)], inv=True)][:m]