LIMIT = 10**6
spf = list(range(LIMIT+1))
primes = []

# If p is prime, spf[p] == p
p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2

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
