L = []; R = []; LC = []; RC = []; S = []; Z = []

# to be modified
INIT = 0
def combine(a, b):
    return a+b
def accumulate(a, b):
    return a+b

def create(l, r):
    L.append(l); R.append(r); LC.append(-1); RC.append(-1); S.append(INIT); Z.append(INIT)
    return len(L)-1
def push(i):
    l = L[i]; r = R[i]
    if l == r: return
    mi = (l+r)>>1
    if LC[i] < 0: LC[i] = create(l, mi); RC[i] = create(mi+1, r)
    lc = LC[i]; rc = RC[i]; z = Z[i]
    # to be modified
    S[lc] = accumulate(S[lc], z*(mi-l+1)); S[rc] = accumulate(S[rc], z*(r-mi))
    Z[lc] = accumulate(Z[lc], z); Z[rc] = accumulate(Z[rc], z)
    Z[i] = INIT
def update(lq, rq, v, i=0):
    stk = [(i, 0)]
    while stk:
        i, b = stk.pop()
        if b>0: S[i] = combine(S[LC[i]], S[RC[i]])
        else:
            l = L[i]; r = R[i]
            if l > rq or r < lq: continue
            if l >= lq and r <= rq:
                # to be modified
                S[i] = accumulate(S[i], v*(r-l+1)); Z[i] = accumulate(Z[i], v)
                continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
def get(lq, rq, i=0):
    stk = [(i, 0)]; tmp = []
    while stk:
        i, b = stk.pop()
        if b>0: tmp.append(combine(tmp.pop(), tmp.pop()))
        else:
            l = L[i]; r = R[i]
            if l > rq or r < lq: tmp.append(INIT); continue
            if l >= lq and r <= rq: tmp.append(S[i]); continue
            push(i); stk.append((i, 1)); stk.append((LC[i], 0)); stk.append((RC[i], 0))
    return tmp[0]

if __name__ == '__main__':
    T = create(0, 10)
    # inclusive add
    update(1, 3, 2)
    update(2, 5, -1)
    update(7, 9, 7)
    print(get(0, 10)) # 23
    print([get(i, i) for i in range(11)]) # [0, 2, 1, 1, -1, -1, 0, 7, 7, 7, 0]