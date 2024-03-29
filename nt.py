# GCD of a and b, or use math.gcd
def gcd(a, b):
    while b: a, b = b, a % b
    return a

# LCM of a and b
def lcm(a,b):
    return a * b // gcd(a,b)

# Returns (x, y) such that ax + by = 1
# Assumption: gcd(a, b) = 1
def bezout(a, b):
    if a == 0:
        return 0, 1
    elif b == 0:
        return 1, 0
    else:
        p, q = bezout(b, a % b)
        return (q, p - q * (a // b))

# Used for inv_mod
def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else: g, y, x = egcd(b % a, a); return (g, x - (b // a) * y, y)

# Inverse modulo, i.e. x such that a^x = 1 mod m, or just use the builtin pow(a, -1, m)
def inv_mod(a, m):
    g, x, _ = egcd(a, m)
    if g != 1: raise Exception
    else: return x % m

# CRT, x mod lcm(m, n) where x = a mod m and x = b mod n
def crt(a, m, b, n):
    d = gcd(m, n)
    k = m * n // d
    if (a - b) % d != 0:
        print('no solution')
    else:
        u, _ = bezout(m, n)
        return (a - m * u * (a - b) // d) % k

# a^b % m, or just use the builtin pow function
def powmod(a, b, m):
    if b == 0:
        return 1
    elif b == 1:
        return a % m
    elif b % 2:
        return a * powmod(a * a % m, b // 2, m) % m
    return powmod(a * a % m, b // 2, m)

def binmod(n, r, m):
    if r > n: return 0
    if r == 0 or r == n: return 1
    if n < m:
        # compute nCr as usual
        s = 1
        for i in range(m): s *= (n-i)*pow(i+1, -1, m); s %= m
    else:
        s = 1
        while n: s = s*binmod(n%m, r%m, m)%m; n //= m; r //= m
    return s

# Checks if p is probably prime
# exclude 2 from the check since it's obvious
# use pow instead of powmod to remove dependency
from random import randint
def miller_rabin(p):
    if p % 2 == 0: return 0
    if p == 3: return 1
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(3):
        x = pow(randint(2, p-2), d, p)
        for _ in range(s):
            y = x**2 % p
            if y == 1 and x != 1 and x != p-1: return 0
            x = y
        if y != 1: return 0
    return 1

# Another variant
from random import randint
def miller_rabin(p):
    if p % 2 == 0: return 0
    if p == 3: return 1
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(3):
        x = pow(randint(2, p-2), d, p)
        if x == 1 or x == p-1: continue
        ok = 0
        for _ in range(s):
            x = x*x%p
            if x == 1: return 0
            if x == p-1: ok = 1; break
        if not ok: return 0
    return 1

# Output a trivial factor of n, can factorize integers faster
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