# ternary search, finding n that minimizes f in [a, b]
def f(n): return n**2-1440*n+8239

# floating point version
a, b = 0, 10**9
gr = (5**0.5-1)/2
tol = 1e-9
while b-a>tol:
    λ, μ = gr*a + (1-gr)*b, (1-gr)*a + gr*b
    if f(μ) > f(λ): b = μ
    else: a = λ
print((a+b)/2)

# integer version
a, b = 0, 10**9
while b-a>2:
    λ, μ = a+(b-a)//3, b-(b-a)//3
    if f(μ) > f(λ): b = μ
    else: a = λ
print(min(range(a-2, b+3), key=f))