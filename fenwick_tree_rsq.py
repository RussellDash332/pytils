# the classic PURQ version
class FenwickTree:
    def __init__(self, arr):
        self.ft = [0]*(len(arr)+1); self.n = len(arr)
        for i, e in enumerate(arr): self.add(i, e)
    def add(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] += e; idx += idx&(-idx)
    def get(self, idx):
        s, idx = 0, min(idx, self.n)
        while idx > 0: s += self.ft[idx]; idx -= idx&(-idx)
        return s

# RURQ version
class FenwickTree:
    def __init__(self, arr):
        self.ft1 = [0]*(len(arr)+1)
        self.ft2 = [0]*(len(arr)+1)
        self.n = len(arr)
        for i in range(self.n): self.add(i, i+1, arr[i])
    def add(self, l, r, v):
        r = min(r, self.n); p1 = l+1; p2 = r+1
        while p1 <= self.n: self.ft1[p1] += v; self.ft2[p1] += v*l; p1 += p1&(-p1)
        while p2 <= self.n: self.ft1[p2] -= v; self.ft2[p2] -= v*r; p2 += p2&(-p2)
    def get(self, l, r):
        r = min(r, self.n); s1 = s2 = s3 = s4 = 0; p1 = r; p2 = l
        while p1 > 0: s1 += self.ft1[p1]; s2 += self.ft2[p1]; p1 -= p1&(-p1)
        while p2 > 0: s3 += self.ft1[p2]; s4 += self.ft2[p2]; p2 -= p2&(-p2)
        return s1*r-s2-s3*l+s4

# PURQ but 2D
class FenwickTree2D:
    def __init__(self, r, c):
        self.ft = [0]*(r+1)*(c+1); self.r = r; self.c = c
    def add(self, r, c, e):
        r += 1; c += 1
        while r <= self.r:
            cc = c
            while cc <= self.c: self.ft[r*(self.c+1)+cc] += e; cc += cc&(-cc)
            r += r&(-r)
    def get(self, r, c):
        s = 0
        while r > 0:
            cc = c
            while cc > 0: s += self.ft[r*(self.c+1)+cc]; cc -= cc&(-cc)
            r -= r&(-r)
        return s

if __name__ == '__main__':
    arr = [1, 4, 2, 8, 3, 5, 3, 1]
    ft = FenwickTree(arr)
    print(ft.get(0, 1) == sum(arr[0:1]))
    print(ft.get(0, 3) == sum(arr[0:3]))
    print(ft.get(3, 10) == sum(arr[3:10]))
    ft.add(0, 1, 10) # [11, 4, 2, 8, 3, 5, 3, 1]
    for i in range(0, 1): arr[i] += 10
    print(ft.get(0, 1) == sum(arr[0:1]))
    print(ft.get(0, 3) == sum(arr[0:3]))
    print(ft.get(3, 10) == sum(arr[3:10]))
    ft.add(4, 5, 1000) # [11, 4, 2, 8, 1003, 5, 3, 1]
    for i in range(4, 5): arr[i] += 1000
    print(ft.get(0, 1) == sum(arr[0:1]))
    print(ft.get(0, 3) == sum(arr[0:3]))
    print(ft.get(3, 10) == sum(arr[3:10]))
    ft.add(1, 6, 2) # [11, 6, 4, 10, 1005, 7, 5, 1]
    for i in range(1, 6): arr[i] += 2
    print(ft.get(0, 1) == sum(arr[0:1]))
    print(ft.get(0, 3) == sum(arr[0:3]))
    print(ft.get(3, 10) == sum(arr[3:10]))

    arr = [
        [1, 2, 4, 8, 16],
        [3, -2, 1, 4, 5],
        [7, 17, -2, 3, -45]
    ]
    ft = FenwickTree2D(len(arr), len(arr[0]))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            ft.add(i, j, arr[i][j])
    from random import *
    for _ in range(30): # 30 random checks
        assert ft.get(x:=randint(1, len(arr)), y:=randint(1, len(arr[0]))) == sum(arr[i][j] for i in range(x) for j in range(y))