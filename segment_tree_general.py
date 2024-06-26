class SegTree:
    def __init__(self, a, f, d):
        self.n = 1<<(len(bin(len(a)-1))-2)
        self.a = a + [d]*(self.n - len(a))
        self.t = [0]*(4*self.n)
        self.l = [None]*(4*self.n)
        self.f = f
        def b(p, l, r):
            if l == r: self.t[p] = self.a[l]
            else:
                m = (l+r)//2
                b(2*p, l, m), b(2*p+1, m+1, r)
                self.t[p] = f(self.t[2*p], self.t[2*p+1])
        b(1, 0, self.n-1)
    def g(self, a, b):
        if a == None: return b
        if b == None: return a
        return self.f(a, b)
    def push(self, p, l, r):
        if self.l[p] != None:
            self.t[p] = self.l[p]
            if l != r:  self.l[2*p] = self.l[2*p+1] = self.l[p]
            else:       self.a[l] = self.l[p]
            self.l[p] = None
    def rq(self, p, l, r, i, j):
        self.push(p, l, r)
        if i > j: return None
        if l >= i and r <= j: return self.t[p]
        m = (l + r)//2
        return self.g(
            self.rq(2*p, l, m, i, min(m, j)),
            self.rq(2*p+1, m+1, r, max(i, m+1), j)
        )
    def ru(self, p, l, r, i, j, v):
        self.push(p, l, r)
        if i > j: return
        if l >= i and r <= j:
            self.l[p] = v
            self.push(p, l, r)
        else:
            m = (l+r)//2
            self.ru(2*p, l, m, i, min(m, j), v), self.ru(2*p+1, m+1, r, max(i, m+1), j, v)
            self.t[p] = self.g(
                self.l[2*p] if self.l[2*p] != None else self.t[2*p],
                self.l[2*p+1] if self.l[2*p+1] != None else self.t[2*p+1]
            )
    def get(self, i, j):
        return self.rq(1, 0, self.n-1, i, j-1)
    def update(self, i, j, v):
        self.ru(1, 0, self.n-1, i, j-1, v)

class MinSegTree(SegTree):
    def __init__(self, a):
        super().__init__(a, min, float('inf'))

class MaxSegTree(SegTree):
    def __init__(self, a):
        super().__init__(a, max, -float('inf'))

class SumSegTree(SegTree):
    def __init__(self, a):
        def sum2(*x):
            if len(x) == 1: return sum(*x)
            return sum(x)
        super().__init__(a, sum2, 0)

class ProdSegTree(SegTree):
    def __init__(self, a):
        def product(*n):
            if len(n) == 1: n = n[0]
            r = 1
            for i in n: r *= i
            return r
        super().__init__(a, product, 1)

arr = [10, 1, 7, 8, 2, 3, 6, 5, 4, 9]
min_st = MinSegTree(arr.copy())
max_st = MaxSegTree(arr.copy())
sum_st = SumSegTree(arr.copy())
prod_st = ProdSegTree(arr.copy())

for name, segtree in [('min', min_st), ('max', max_st), ('sum', sum_st), ('prod', prod_st)]:
    print(f'Querying {name}...')
    arr2 = arr.copy()
    print(arr2)
    print(segtree.get(1, 6), segtree.f(arr2[1:6])) # [1, 7, 8, 2, 3]
    print(segtree.get(0, 2), segtree.f(arr2[0:2])) # [10, 1]
    print(segtree.get(7, 10), segtree.f(arr2[7:10])) # [5, 4, 9]
    print()

    print(f'Updating {name}...')
    arr2 = arr.copy()
    arr2[2] = 999
    segtree.update(2, 3, 999) # [10, 1, 999, 8, 2, 3, 6, 5, 4, 9]
    print(arr2)
    print(segtree.get(1, 6), segtree.f(arr2[1:6])) # [1, 999, 8, 2, 3]
    print(segtree.get(0, 2), segtree.f(arr2[0:2])) # [10, 1]
    print(segtree.get(7, 10), segtree.f(arr2[7:10])) # [5, 4, 9]
    print()

    print(f'Updating {name} again...')
    arr2 = arr.copy()
    arr2[2], arr2[9] = 999, -1000
    segtree.update(9, 10, -1000) # [10, 1, 999, 8, 2, 3, 6, 5, 4, -1000]
    print(arr2)
    print(segtree.get(1, 6), segtree.f(arr2[1:6])) # [1, 999, 8, 2, 3]
    print(segtree.get(0, 2), segtree.f(arr2[0:2])) # [10, 1]
    print(segtree.get(7, 10), segtree.f(arr2[7:10])) # [5, 4, -1000]
    print()