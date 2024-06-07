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