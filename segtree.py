from math import ceil, log2

class SegTree:
    def __init__(self, arr, fn, default):
        sz = 2**ceil(log2(len(arr)))
        self.n, self.fn, self.default = len(arr), fn, default
        self.st = [None] + [0]*(2*int(sz)-1)
        def helper(s=0, e=len(arr)-1, i=1):
            if s == e:
                self.st[i] = arr[s]
                return arr[s]
            mid = (s + e) // 2
            self.st[i] = fn([helper(s, mid, 2*i), helper(mid+1, e, 2*i+1)])
            return self.st[i]
        helper()

    def get(self, s, e): # fn(self[s:e])
        e -= 1
        def helper(ss=0, se=self.n-1, i=1):
            if s <= ss and e >= se: return self.st[i]
            if se < s or ss > e:    return self.default
            mid = (ss + se) // 2
            return self.fn([helper(ss, mid, 2*i), helper(mid+1, se, 2*i+1)])
        return helper()

    def update(self, idx, val):
        def helper(s=0, e=self.n-1, i=1):
            if idx < s or idx > e: return
            if s != e:
                mid = (s + e) // 2
                helper(s, mid, 2*i)
                helper(mid+1, e, 2*i+1)
                self.st[i] = self.fn([self.st[2*i], self.st[2*i+1]])
            else:
                self.st[i] = val
        helper()

class MinSegTree(SegTree):
    def __init__(self, arr):
        super().__init__(arr, min, float('inf'))

class MaxSegTree(SegTree):
    def __init__(self, arr):
        super().__init__(arr, max, -float('inf'))

class SumSegTree(SegTree):
    def __init__(self, arr):
        super().__init__(arr, sum, 0)

class ProdSegTree(SegTree):
    def __init__(self, arr):
        def product(args):
            r = 1
            for i in args: r *= i
            return r
        super().__init__(arr, product, 1)

arr = [10, 1, 7, 8, 2, 3, 6, 5, 4, 9]
min_st = MinSegTree(arr.copy())
max_st = MaxSegTree(arr.copy())
sum_st = SumSegTree(arr.copy())
prod_st = ProdSegTree(arr.copy())

for name, segtree in [('min', min_st), ('max', max_st), ('sum', sum_st), ('prod', prod_st)]:
    print(f'Querying {name}...')
    arr2 = arr.copy()
    print(arr2)
    print(segtree.get(1, 6), segtree.fn(arr2[1:6])) # [1, 7, 8, 2, 3]
    print(segtree.get(0, 2), segtree.fn(arr2[0:2])) # [10, 1]
    print(segtree.get(7, 10), segtree.fn(arr2[7:10])) # [5, 4, 9]
    print()

    print(f'Updating {name}...')
    arr2 = arr.copy()
    arr2[2] = 999
    segtree.update(2, 999) # [10, 1, 999, 8, 2, 3, 6, 5, 4, 9]
    print(arr2)
    print(segtree.get(1, 6), segtree.fn(arr2[1:6])) # [1, 999, 8, 2, 3]
    print(segtree.get(0, 2), segtree.fn(arr2[0:2])) # [10, 1]
    print(segtree.get(7, 10), segtree.fn(arr2[7:10])) # [5, 4, 9]
    print()

    print(f'Updating {name} again...')
    arr2 = arr.copy()
    arr2[2], arr2[9] = 999, -1000
    segtree.update(9, -1000) # [10, 1, 999, 8, 2, 3, 6, 5, 4, -1000]
    print(arr2)
    print(segtree.get(1, 6), segtree.fn(arr2[1:6])) # [1, 999, 8, 2, 3]
    print(segtree.get(0, 2), segtree.fn(arr2[0:2])) # [10, 1]
    print(segtree.get(7, 10), segtree.fn(arr2[7:10])) # [5, 4, -1000]
    print()