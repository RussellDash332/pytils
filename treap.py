from random import random
class Node:
    def __init__(s, val): s.val = val; s.p = random(); s.l = s.r = None; s.rev = s.cnt = 0

def cnt(t): return t.cnt if t else 0
def update(t):
    if t: t.cnt = cnt(t.l) + cnt(t.r) + 1
def push(t):
    if not t or not t.rev: return
    t.rev = False; t.l, t.r = t.r, t.l
    if t.l: t.l.rev ^= 1
    if t.r: t.r.rev ^= 1
def split(t, val, add=0):
    if not t: return None, None
    else:
        push(t)
        if val <= (k:=add+cnt(t.l)): l, t.l = split(t.l, val, add); update(t); return l, t
        else:                           t.r, r = split(t.r, val, k+1); update(t); return t, r
def merge(l, r):
    push(l), push(r)
    if (not l) or (not r): t = l or r
    elif l.p < r.p: l.r = merge(l.r, r); t = l
    else: r.l = merge(l, r.l); t = r
    update(t); return t
def insert(t, val):
    l, r = split(t, float('inf'))
    return merge(merge(l, Node(val)), r)
def reverse(t, a, b):
    t1, t2 = split(t, a); t2, t3 = split(t2, b-a)
    if t2: t2.rev ^= 1
    return merge(merge(t1, t2), t3)
def inorder(t):
    if not t: return
    push(t), inorder(t.l), print(t.val, end=' '), inorder(t.r)

treap = None
for i in [1, 2, 3, 10, 9, 8, 7, 6, 5, 4]: treap = insert(treap, i)
inorder(treap), print()         # 1 2 3 10 9 8 7 6 5 4
treap = reverse(treap, 3, 10)
inorder(treap), print()         # 1 2 3 4 5 6 7 8 9 10
treap = reverse(treap, 1, 5)
inorder(treap), print()         # 1 5 4 3 2 6 7 8 9 10