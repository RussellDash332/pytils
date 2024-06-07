# Using suffix array
def smm(s, pp):
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

if __name__ == '__main__':
    s = 'banana boy likes apple boys'
    pp = ['a', 'na', 'boy', 'p', 'orange']
    print(smm(s, pp))