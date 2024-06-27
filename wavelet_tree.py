# Work in progress
# https://codeforces.com/blog/entry/52854
class Node:
    def __init__(s, a, l, h):
        s.l = l; s.h = h; s.lc = s.rc = None
        if l == h: s.f = [*range(len(a)+1)]; return
        m = (l+h)//2; s.f = []; la = []; ra = []
        for i in range(len(a)):
            if a[i] <= m: la.append(a[i]); s.f.append(s.f[-1]+1)
            else: ra.append(a[i]); s.f.append(s.f[-1])
        s.lc = Node(la, l, m); s.rc = Node(ra, l, m)