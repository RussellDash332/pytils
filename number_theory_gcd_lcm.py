# GCD of a and b, or use math.gcd
def gcd(a, b):
    while b: a, b = b, a%b
    return a

# LCM of a and b, on higher Python versions math.lcm is provided
def lcm(a, b):
    return a*b//gcd(a, b)