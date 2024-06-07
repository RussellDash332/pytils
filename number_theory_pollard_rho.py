# Output a trivial factor of n, can factorize integers faster
from math import gcd
def pollard_rho(n):
    c = 1
    while True:
        x, y, d = 2, 2, 1
        while d == 1: 
            x = (x*x+c)%n
            y = (y*y+c)%n; y = (y*y+c)%n
            d = gcd(abs(x-y), n)
        if d != n: return d
        else: c += 1

print(pollard_rho(105))
print(pollard_rho(10**9+3)) # not a prime