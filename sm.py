def kmp(T, P):
    n, m = len(T), len(P)
    b = [0]*(m+1)
    i, j = 0, -1
    b[0] = -1
    while i < m:
        while j >= 0 and P[i] != P[j]: j = b[j]
        i += 1; j += 1; b[i] = j
    i = j = 0
    matches = []
    while i < n:
        while j >= 0 and T[i] != P[j]: j = b[j]
        i += 1; j += 1
        if j == m: matches.append(i-m); j = b[j]
    return matches

if __name__ == '__main__':
    P = 'na'
    T = 'banana boy likes native americanas'
    print(kmp(T, P))