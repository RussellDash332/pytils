# Output a trivial factor of n, can factorize integers faster
from math import gcd
def pollard_rho(n):
    c = 1
    while True:
        x, y, d = 2, 2, 1
        while d == 1: x = (x*x+c)%n; y = (y*y+c)%n; y = (y*y+c)%n; d = gcd(abs(x-y), n)
        if d != n: return d
        c += 1

# With Brent modification
# Credits: Brandon Tang
from math import gcd; from random import *
def pollard_rho_brent(n):
    while True:
        y = randint(1, n-1); c = randint(1, n-1); m = randint(1, n-1); g = r = q = 1
        while g == 1:
            x = y; k = 0
            for _ in range(r): y = (y*y+c)%n
            while k < r and g == 1:
                s = y
                for _ in range(min(m, r-k)): y = (y*y+c)%n; q = q*abs(x-y)%n
                g = gcd(q, n); k += m
            r *= 2
        if g == n: g = 1
        while g == 1: s = (s*s+c)%n; g = gcd(abs(x-s), n)
        if g != n: return g

print(pollard_rho(105))
print(pollard_rho(10**9+3)) # not a prime

print(pollard_rho_brent(105))
print(pollard_rho_brent(10**9+3)) # not a prime