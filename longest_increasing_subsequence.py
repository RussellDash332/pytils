# LIS, to make it non-decreasing just add equal sign to the inequality signs
def lis(arr):
    if not arr: return []
    def upper_bound(sub, idx):
        lo, hi = 0, len(sub) - 1
        while hi > lo:
            mid = (lo + hi) // 2
            if arr[sub[mid]] < arr[idx]: lo = mid + 1
            else: hi = mid
        return hi
    temp = []; par = [None]*len(arr)
    for i in range(len(arr)):
        if not temp or arr[i] > arr[temp[-1]]:
            if temp: par[i] = temp[-1]
            temp.append(i)
        else:
            rep = upper_bound(temp, i); temp[rep] = i
            if rep != 0: par[i] = temp[rep - 1]
    final = []; curr = temp[-1]
    while curr != None: final.append(curr); curr = par[curr]
    return final[::-1]

# https://stackoverflow.com/questions/22923646/number-of-all-longest-increasing-subsequences
from bisect import *
def count_lis(A, distinct=True):
    B = []; P = []
    for e in A:
        p = bisect(B, e-1, key=lambda x: x[-1][0])
        if p == len(B): P.append([0]); B.append([])
        u = P[p-1][-1]-P[p-1][bisect(B[p-1], -e, key=lambda x: -x[0])] if p else 1
        if not distinct: B[p].append((e, u)); P[p].append(P[p][-1]+u)
        elif B[p] and B[p][-1][0] == e: B[p][-1] = (e, u); P[p][-1] = P[p][-2]+u
        else: B[p].append((e, u)); P[p].append(P[p][-1]+u)
    return len(B), sum(b[1] for b in B[-1]) if B else 0

if __name__ == '__main__':
    # general (1)
    A = [3, 2, 2, 4, 5, 8, 7]
    print(lis(A))
    print(count_lis(A))

    # general (2)
    A = [52, 81, 43, 81, 18, 85, 71, 87]
    print(lis(A))
    print(count_lis(A))

    # general (2)
    A = [16, 5, 8, 6, 1, 10, 5, 2, 15, 3, 2, 4, 1]
    print(lis(A))
    print(count_lis(A))

    # empty
    A = []
    print(lis(A))
    print(count_lis(A))

    # increasing
    A = [1, 2, 3, 4, 5, 6]
    print(lis(A))
    print(count_lis(A))

    # same
    A = [1]*10
    print(lis(A))
    print(count_lis(A))

    from random import *
    # random distinct
    a = [*range(10**4)]
    shuffle(a)
    print(len(lis(a)))
    print(count_lis(a))

    # random general (1)
    a = [randint(1, 100) for _ in range(10**4)]
    print(len(lis(a)))
    print(count_lis(a))

    # random general (2)
    a = [randint(-10**18, 10**18) for _ in range(10**5)]
    print(len(lis(a)))
    print(count_lis(a))