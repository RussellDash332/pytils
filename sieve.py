LIMIT = 432
sieve = [True] * (LIMIT + 1)
primes = []

p = 2
while p <= LIMIT:
    if sieve[p]:
        primes.append(p)
        for i in range(2*p, LIMIT, p):
            sieve[i] = False
    if p == 2:
        p -= 1
    p += 2