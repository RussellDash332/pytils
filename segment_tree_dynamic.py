class Node:
    def __init__(s, l, r):
        s.l = l; s.r = r; s.lc = s.rc = None; s.s = s.z = 0
    def push(s):
        if s.l == s.r: return
        mi = (s.l+s.r)//2
        if not s.lc: s.lc = Node(s.l, mi); s.rc = Node(mi+1, s.r)
        s.lc.s += s.z*(mi-s.l+1); s.lc.z += s.z; s.rc.s += s.z*(s.r-mi); s.rc.z += s.z; s.z = 0
    def add(s, lq, rq, v):
        if s.l > rq or s.r < lq: return
        if s.l >= lq and s.r <= rq: s.s += v*(s.r-s.l+1); s.z += v; return
        s.push(); s.lc.add(lq, rq, v); s.rc.add(lq, rq, v); s.s = s.lc.s+s.rc.s
    def get(s, lq, rq):
        if s.l > rq or s.r < lq: return 0
        if s.l >= lq and s.r <= rq: return s.s
        s.push(); return s.lc.get(lq, rq)+s.rc.get(lq, rq)

if __name__ == '__main__':
    T = Node(0, 10)
    # inclusive add
    T.add(1, 3, 2)
    T.add(2, 5, -1)
    T.add(7, 9, 7)
    print(T.get(0, 10))
    print([T.get(i, i) for i in range(11)])