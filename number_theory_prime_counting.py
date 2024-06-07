LIMIT = 10**6
spf = list(range(LIMIT+1))
primes = [2]; p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

# Meissel-Lehmer Algorithm
mem = {}
def phi(x, a):
    if (x, a) in mem: return mem[(x, a)]
    if a == 1: return (x + 1)//2
    mem[(x, a)] = phi(x, a-1) - phi(x//primes[a-1], a-1)
    return mem[(x, a)]

from bisect import *
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

# Golfed black magic! Tested on /primecount and /frumtolutalning
def pi(n):
    if n < 2: return 0
    v,r,j=int(n**0.5),n-1,1
    h,l,u=[0]*(v+1),[0]*(v+1),[0]*(v+1)
    for p in range(2,v+1):l[p],h[p]=p-1,n//p-1
    for p in range(2,v+1):
        if l[p]==l[p-1]:continue
        t,e=l[p-1],min(v,n//(p*p))
        r-=h[p]-t
        for i in range(p+j,e+1,j):
            if u[i]:continue
            d,x=i*p,((i*p)>v)&1
            h[i]-=[h,l][x][[d,n//d][x]]-t
        for i in range(v,p*p-1,-1):l[i]-=l[i//p]-t
        for i in range(p*p,e+1,p):u[i]=1
        if p==2:j+=1
    return r