LIMIT = 10**6
spf = list(range(LIMIT+1))

# If p is prime, spf[p] == p
primes = []; p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2

# Alternative approach
primes = [2]; p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

# Prime factorization
def pf(n):
    res = []; idx = k = 0
    while n != 1 and idx < len(primes):
        pp = primes[idx]
        if pp*pp > n: break
        if n % pp == 0:
            while n % pp == 0: n //= pp; k += 1
            if k: res.append((pp, k))
        idx += 1; k = 0
    if n != 1: res.append((n, 1))
    return res

# Number of divisors
def ndiv(n):
    res = 1; idx = k = 0
    while n != 1 and idx < len(primes):
        pp = primes[idx]
        if pp*pp > n: break
        if n % pp == 0:
            while n % pp == 0: n //= pp; k += 1
            if k: res *= k+1
        idx += 1; k = 0
    if n != 1: res *= 2
    return res

# Euler's totient function
def tot(n):
    res = n
    for p, _ in pf(n): res //= p; res *= p-1
    return res

# Meissel-Lehmer Algorithm
mem = {}
def phi(x, a):
    if (x, a) in mem: return mem[(x, a)]
    if a == 1: return (x + 1)//2
    mem[(x, a)] = phi(x, a-1) - phi(x//primes[a-1], a-1)
    return mem[(x, a)]

from bisect import bisect
def pi(x):
    if x in mem: return mem[x]
    if x <= LIMIT:
        mem[x] = bisect(primes, x)
        return mem[x]
    a, b, c = pi(int(x**0.25)), pi(int(x**0.5)), pi(int(x**(1/3)))
    r = phi(x, a) + (b+a-2)*(b-a+1)//2
    for i in range(a+1, b+1):
        w = x//primes[i-1]
        r -= pi(w)
        if i <= c:
            for j in range(i, pi(int(w**0.5))+1): r -= pi(w//primes[j-1])-j+1
    mem[x] = r
    return r