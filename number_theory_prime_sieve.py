from array import *
LIMIT = 10**6
F = array('I', [0]*LIMIT)
P = array('I')

# If p>=2 is prime, F[p] == p (F = smallest prime factor)
for i in range(2, LIMIT):
    if F[i] < 1: F[i] = i; P.append(i)
    for p in P:
        if (j:=i*p) >= LIMIT: break
        F[j] = p
        if p == F[i]: break