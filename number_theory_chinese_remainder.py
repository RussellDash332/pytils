from math import gcd

# Returns (x, y) such that ax + by = 1
# Assumption: gcd(a, b) = 1
def bezout(a, b):
    if a == 0: return 0, 1
    elif b == 0: return 1, 0
    else: p, q = bezout(b, a%b); return (q, p-a//b*q)

# CRT, x mod lcm(m, n) where x = a mod m and x = b mod n
def crt(a, m, b, n):
    d = gcd(m, n); k = m*n//d
    if (a-b)%d: raise Exception('no solution')
    else: return (a-m*bezout(m, n)[0]*(a-b)//d)%k

print(crt(3, 5, 2, 7)) # 23 since 23 = 3 mod 5 = 2 mod 7