class FenwickTree:
    def __init__(self, arr):
        self.ft = [0]*(len(arr)+1)
        self.n = len(arr)
        for i, e in enumerate(arr):
            self.add(i, e)
    def add(self, idx, e): # arr[idx] += e
        idx += 1
        while idx <= self.n:
            self.ft[idx] += e
            idx += idx & (-idx) # largest power of 2 that divides idx
    def get(self, idx): # sum(arr[:idx])
        s, idx = 0, min(idx, self.n)
        while idx > 0:
            s, idx = s+self.ft[idx], idx-(idx&(-idx))
        return s

ft = FenwickTree([1, 4, 2, 8, 3, 5, 3, 1])
print(ft.get(1))
print(ft.get(3))
print(ft.get(10))
ft.add(0, 10) # [11, 4, 2, 8, 3, 5, 3, 1]
print(ft.get(1))
print(ft.get(3))
print(ft.get(10))
ft.add(4, 1000) # [11, 4, 2, 8, 1003, 5, 3, 1]
print(ft.get(1))
print(ft.get(3))
print(ft.get(10))