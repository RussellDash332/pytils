'''
Tonelli-Shanks algorithm
Given an integer n and a prime number p, find r such that r^2 = n (mod p)

Cornacchia algorithm
Solve for nonnegative integers (x, y) such that x^2 + dy^2 = p where p is prime
For non-prime integers, don't use Tonelli-Shanks :)
'''

def tonelli_shanks(n, p):
    if pow(n, (p-1)//2, p) == p-1: return None # n is a quadratic non-residue
    q = p-1; s=0
    while q%2 == 0: q //= 2; s += 1
    for z in range(2, p):
        if p-1 == pow(z, (p-1)//2, p): break # z is a quadratic non-residue
    c = pow(z, q, p); r = pow(n, (q+1)//2, p); t = pow(n, q, p); m = s
    while (t-1)%p:
        u = t*t%p; i = -1
        for i in range(1, m):
            if u%p == 1: break
            u = u*u%p
        if i == -1: return None
        b = pow(c, 1<<(m-i-1), p); r = r*b%p; c = b*b%p; t = t*c%p; m = i
    return r

def cornacchia(d, p):
    r = tonelli_shanks(-d, p)
    if r == None: return None
    z = [p, min(r, p-r)]
    while z[-1]**2 >= p: z.append(z[-2]%z[-1])
    x, y = z[-1], round(((p-z[-1]**2)/d)**0.5)
    if x*x + d*y*y == p: return x, y

if __name__ == '__main__':
    print(tonelli_shanks(2, 7))     # 4^2 = 2 (mod 7)
    print(tonelli_shanks(5, 13))    # no solution to x^2 = 5 (mod 13)

    print(cornacchia(1, 73))        # 8^2 + 1*3^2 = 73
    print(cornacchia(47, 13907))    # 18^2 + 47*17^2 = 13907
    print(cornacchia(19, 73))       # no solution to x^2 + 19y^2 = 73