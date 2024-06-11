S = 'aabacab'

N = len(S); s = '@#'+'#'.join(S)+'#^'; p = [0]*(2*N+3); l = r = 1
for i in range(2*N+2):
    p[i] = max(0, min(r-i, p[l+r-i]))
    while s[i-p[i]] == s[i+p[i]]: p[i] += 1
    if i+p[i] > r: l = i-p[i]; r = i+p[i]

print('Odd-length:', [p[2*i+2]//2 for i in range(N)]) # index i = number of subpalindromes centered at s[i]
print('Even-length:', [p[2*i+1]//2 for i in range(N)]) # index i(>0) = number of subpalindromes centered at s[i-1]+s[i]