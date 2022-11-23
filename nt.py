# GCD of a and b
def gcd(a, b):
    while b:
        a, b = b, a % b
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
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Inverse modulo, i.e. x such that a^x = 1 mod m
def inv_mod(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception
    else:
        return x % m