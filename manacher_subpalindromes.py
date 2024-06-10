S = 'aabacab'; N = len(S)

s = '@#'+'#'.join(S)+'#^'
n = len(s)-2; p = [0]*(n+2); l = r = 1
for i in range(n+1):
    p[i] = max(0, min(r-i, p[l+r-i]))
    while s[i-p[i]] == s[i+p[i]]: p[i] += 1
    if i+p[i] > r: l = i-p[i]; r = i+p[i]
do = [0]*N; de = [0]*N
for i in range(1, 2*N, 2): de[i//2] = p[i]//2
for i in range(2, 2*N+1, 2): do[i//2-1] = p[i]//2

print(S)
print('Odd-length:', do)
print('Even-length:', de)