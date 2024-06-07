def binmod(n, r, m):
    if r > n: return 0
    if r == 0 or r == n: return 1
    if n < m:
        # compute nCr as usual
        s = 1
        for i in range(r): s *= (n-i)*pow(i+1, -1, m); s %= m
    else:
        s = 1
        while n: s = s*binmod(n%m, r%m, m)%m; n //= m; r //= m
    return s

print(binmod(10**8+3, 42069, 15485863))