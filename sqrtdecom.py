from math import ceil
class Sqrt:
    def __init__(self, arr):
        self.a = arr
        self.b = [0]*ceil(len(arr)**0.5)
        self.n = len(self.b)
        for i in range(len(arr)): self.b[i//self.n] += arr[i]
    def update(self, x, v):
        self.b[x//self.n] -= self.a[x]; self.a[x] = v; self.b[x//self.n] += v
    def query(self, l, r):
        q = 0
        for i in range(r//self.n): q += self.b[i]
        for i in range(r//self.n*self.n, r): q += self.a[i]
        for i in range(l//self.n): q -= self.b[i]
        for i in range(l//self.n*self.n, l): q -= self.a[i]
        return q

if __name__ == '__main__':
    from random import randint
    arr = [0]*11
    arr2 = arr.copy()
    sq = Sqrt(arr)
    for i, v in [(1, 10), (5, 2), (3, 4), (4, -1), (7, 3), (10, 12), (1, 3), (2, 2), (3, -7)]:
        arr2[i] = v
        print('Current array:\t', arr2)
        sq.update(i, v)
        print('Sqrt array:\t', [sq.query(i, i+1) for i in range(11)])
        for _ in range(5):
            a = randint(0, 11); b = a+randint(0, 11-a)
            assert (l:=sum(arr2[a:b])) == (r:=sq.query(a, b)), (a, b, l, r)
        print()
    for _ in range(300):
        a = randint(0, 11); b = a+randint(0, 11-a)
        v = randint(-69420, 42069)
        sq.update(i, v); arr2[i] = v
        assert sq.a == arr2 == (c:=[sq.query(i, i+1) for i in range(11)]), (sq.a, arr2, c)
    print('All done!')