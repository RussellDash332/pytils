from random import *; from array import *
V = array('i'); L = array('i'); R = array('i'); O = array('I'); C = array('I')
P = array('i'); B = array('B'); M = {}
def node(v):
    i = len(V); V.append(v); L.append(-1); R.append(-1); P.append(-1); O.append(randint(1, 10**9)); C.append(1); B.append(0); M.setdefault(v, []).append(i); return i
def cnt(x):
    return C[x] if ~x else 0
def pull(x):
    if ~x:
        C[x] = 1+cnt(L[x])+cnt(R[x])
        if ~L[x]: P[L[x]] = x
        if ~R[x]: P[R[x]] = x
def _push(x):
    if ~x and B[x]:
        B[x] = 0; L[x], R[x] = R[x], L[x]
        if ~L[x]: B[L[x]] ^= 1
        if ~R[x]: B[R[x]] ^= 1
def push(i):
    st = []; q = i
    while ~q: st.append(q); q = P[q]
    while st: _push(st.pop())
def merge(a, b):
    _push(a); _push(b)
    if a < 0 or b < 0:
        z = a if b < 0 else b
        if ~z: P[z] = -1
        return z
    if O[a] < O[b]: R[a] = merge(R[a], b); pull(a); P[a] = -1; return a
    else: L[b] = merge(a, L[b]); pull(b); P[b] = -1; return b
def split(t, k):
    if t < 0: return -1, -1
    _push(t)
    if k <= (z:=cnt(L[t])):
        a, b = split(L[t], k); L[t] = b; pull(t); P[t] = -1
        if ~a: P[a] = -1
        return a, t
    else:
        a, b = split(R[t], ~z+k); R[t] = a; pull(t); P[t] = -1
        if ~b: P[b] = -1
        return t, b
def insert(T, v):
    return merge(T, node(v))
def _rank(i):
    push(i); z = cnt(L[i])+1; q = i
    while ~P[q]:
        p = P[q]
        if R[p] == q: z += cnt(L[p])+1
        q = p
    return z
def rank(T, v):
    if v not in M or not M[v]: return None
    return _rank(M[v][-1])
def erase(T, v):
    if v not in M or not M[v]: return T
    i = M[v].pop()
    if not M[v]: del M[v]
    r = _rank(i); t1, t2 = split(T, r-1); t2, t3 = split(t2, 1); return merge(t1, t3)
def select(T, k):
    q = T
    while q >= 0:
        _push(q); z = cnt(L[q])+1
        if k < z: q = L[q]
        elif k == z: return V[q]
        else: k -= z; q = R[q]
def predecessor(T, v):
    r = rank(T, v)
    if r > 1: return select(T, r-1)
def successor(T, v):
    r = rank(T, v)
    if 0 < r < cnt(T): return select(T, r+1)
def reverse(T, a, b):
    t1, t2 = split(T, a); t2, t3 = split(t2, b-a)
    if ~t2: B[t2] ^= 1
    return merge(merge(t1, t2), t3)
def inorder(t):
    if t < 0: return
    _push(t); inorder(L[t]); print(V[t], end=' '); inorder(R[t])

if __name__ == '__main__':
    # Example
    treap = -1
    for i in [1, 2, 3, 10, 9, 8, 7, 6, 5, 4]: treap = insert(treap, i)
    inorder(treap), print()         # 1 2 3 10 9 8 7 6 5 4

    # reverse test
    treap = reverse(treap, 3, 10)
    inorder(treap), print()         # 1 2 3 4 5 6 7 8 9 10
    treap = reverse(treap, 1, 5)
    inorder(treap), print()         # 1 5 4 3 2 6 7 8 9 10

    # pred + succ + rank + select test
    for i, e in enumerate([1, 5, 4, 3, 2, 6, 7, 8, 9, 10], 1):
        print(predecessor(treap, e), successor(treap, e), rank(treap, e), select(treap, i)==e)

    # erase test
    for i in [7, 1, 10, 4, 3, 2, 6, 5, 9]:
        treap = erase(treap, i)
        inorder(treap), print()
        reverse(treap, 0, 10)
        inorder(treap), print()

    # multiset?
    treap = -1
    for i in sorted([1, 2, 2, 1, -3, -4, 5, 1, 2]): treap = insert(treap, i)
    inorder(treap), print()
    for i in [-4, -3, 1, 2, 5]:
        print(i, rank(treap, i), predecessor(treap, i), successor(treap, i))
    for i in range(9):
        print(i, select(treap, i+1))
    for i in [1, 2, 2, 1, -3, -4, 5, 1, 2]:
        treap = erase(treap, i)
        inorder(treap), print()