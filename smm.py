from collections import deque

# Using suffix array
def smm_sa(s, pp):
    def suffix_array_construction(s):
        n = len(s)
        sa = list(range(n))
        ra = [ord(s[i]) for i in range(n)]
        k, maxi = 1, max(300, n)
        while k < n:
            for kk in [k, 0]:
                c = [0]*maxi
                for i in range(n): c[ra[i+kk] if i+kk<n else 0] += 1
                ss, temp = 0, [0]*n
                for i in range(maxi): t = c[i]; c[i] = ss; ss += t
                for i in range(n):
                    idx = ra[sa[i]+kk] if sa[i]+kk < n else 0
                    temp[c[idx]] = sa[i]
                    c[idx] += 1
                sa = temp
            temp, r = [0]*n, 0
            temp[sa[0]] = r
            for i in range(1, n):
                r += ra[sa[i]] != ra[sa[i-1]] or ra[sa[i]+k] != ra[sa[i-1]+k]
                temp[sa[i]] = r
            ra = temp
            if ra[sa[n-1]] == n-1: break
            k *= 2
        return sa
    s += '\0'
    sa = suffix_array_construction(s)
    n = len(s)
    matches = []
    for p in pp:
        m, lo, hi = len(p), 0, n-1
        while lo < hi:
            mid = (lo+hi)//2
            if s[sa[mid]:sa[mid]+m] >= p: hi = mid
            else: lo = mid+1
        if s[sa[lo]:sa[lo]+m] != p: matches.append([]); continue
        l, hi = lo, n-1
        while lo < hi:
            mid = (lo+hi)//2
            if s[sa[mid]:sa[mid]+m] > p: hi = mid
            else: lo = mid+1
        matches.append(sorted(sa[i] for i in range(l, hi - (s[sa[hi]:sa[hi]+m] != p) + 1)))
    return matches

# Using Aho-Corasick
def smm_ac(s, pp):
    A = 96
    a = [[[-1]*A, 0, -1, []]]
    for w in range(len(pp)):
        n = 0
        for i in range(len(pp[w])):
            idx = ord(pp[w][i])-32
            if a[n][0][idx] == -1: a[n][0][idx] = len(a); a.append([[-1]*A, 0, -1, []])
            n = a[n][0][idx]
        a[n][3].append(w); n = 0
    q = deque()
    for k in range(A):
        if a[0][0][k] == -1:    a[0][0][k] = 0
        elif a[0][0][k] > 0:    a[a[0][0][k]][1] = 0; q.append(a[0][0][k])
    while q:
        r = q.popleft()
        for k in range(A):
            arck = a[r][0][k]
            if arck != -1:
                q.append(arck)
                v = a[r][1]
                while a[v][0][k] == -1: v = a[v][1]
                a[arck][1] = a[arck][2] = a[v][0][k]
                while a[arck][2] != -1 and not a[a[arck][2]][3]: a[arck][2] = a[a[arck][2]][2]
    matches = [[] for _ in range(len(pp))]
    state = ss = 0
    for i in range(len(s)):
        idx = ord(s[i])-32
        while a[ss][0][idx] == -1: ss = a[ss][1]
        a[state][0][idx] = a[ss][0][idx]; state = a[state][0][idx]; ss = state
        while ss != -1:
            for w in a[ss][3]: matches[w].append(i+1-len(pp[w]))
            ss = a[ss][2]
        ss = state
    n = -1
    return matches

if __name__ == '__main__':
    s = 'banana boy likes apple boys'
    pp = ['a', 'na', 'boy', 'p', 'orange']
    print(smm_sa(s, pp))
    print(smm_ac(s, pp))