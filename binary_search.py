def f(n):
    # some function as source of comparison
    # returns True if it works with value n and False otherwise
    return 1

# find lower bound to which it works
# 00000.....00111...11
lo, hi = 0, 10**9
while lo < hi:
    mi = (lo+hi)//2
    if f(mi): hi = mi
    else: lo = mi+1
ans = lo

# find upper bound to which it works
# 11111.....11000...00
lo, hi = 0, 10**9
while hi-lo>1:
    mi = (lo+hi)//2
    if f(mi): lo = mi
    else: hi = mi-1
ans = hi if f(hi) else hi-1

if __name__ == '__main__':
    def f(n): return n**2 > 35
    def g(n): return n**2 < 14
    # find smallest n such that f(n) is True
    lo, hi = 0, 1000
    while lo < hi:
        mi = (lo+hi)//2
        print('Before:\t', lo, mi, hi)
        if f(mi): hi = mi
        else: lo = mi+1
        print('After:\t', lo, mi, hi)
    print('Answer:', lo)
    print('-'*30)
    # find largest n such that g(n) is True
    lo, hi = 0, 1000
    while hi-lo>1:
        mi = (lo+hi)//2
        print('Before:\t', lo, mi, hi)
        if g(mi): lo = mi
        else: hi = mi-1
        print('After:\t', lo, mi, hi)
    print('Answer:', hi if g(hi) else hi-1)