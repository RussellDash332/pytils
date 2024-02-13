# the classic PURQ version
class FenwickTree:
    def __init__(self, arr):
        self.ft = [0]*(len(arr)+1); self.n = len(arr)
        for i, e in enumerate(arr): self.update(i, e)
    def update(self, idx, e):
        idx += 1
        while idx <= self.n: self.ft[idx] += e; idx += idx & (-idx)
    def get(self, idx):
        s, idx = 0, min(idx, self.n)
        while idx > 0: s, idx = s+self.ft[idx], idx-(idx&(-idx))
        return s

# RURQ version
class FenwickTree:
    def __init__(self, arr):
        self.ft1 = [0]*(len(arr)+1)
        self.ft2 = [0]*(len(arr)+1)
        self.n = len(arr)
        for i, e in enumerate(arr): self.add(i, i+1, e)
    def add(self, l, r, v): # arr[l:r] += v
        l += 1; r = min(r, self.n)
        p1, p2, p3, p4 = l, r+1, l, r+1
        while p1 <= self.n: self.ft1[p1] += v; p1 += (p1&(-p1))
        while p2 <= self.n: self.ft1[p2] -= v; p2 += (p2&(-p2))
        while p3 <= self.n: self.ft2[p3] += v*(l-1); p3 += (p3&(-p3))
        while p4 <= self.n: self.ft2[p4] -= v*r; p4 += (p4&(-p4))
    def get(self, l, r): # sum(arr[l:r])
        l += 1; r = min(r, self.n)
        s1 = s2 = s3 = s4 = 0; p1 = p2 = r; p3 = p4 = l-1
        while p1 > 0: s1 += self.ft1[p1]; p1 -= (p1&(-p1))
        while p2 > 0: s2 += self.ft2[p2]; p2 -= (p2&(-p2))
        while p3 > 0: s3 += self.ft1[p3]; p3 -= (p3&(-p3))
        while p4 > 0: s4 += self.ft2[p4]; p4 -= (p4&(-p4))
        return s1*r-s2-s3*(l-1)+s4

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