# Basically z[i] = lcp(s, s[i:])
# Runs in O(n) time
s = 'abacababababcabab'

n = len(s); z = [0]*n; l = r = 0
for i in range(1, n):
    if i < r: z[i] = min(r-i, z[i-l])
    while i+z[i] < n and s[z[i]] == s[i+z[i]]: z[i] += 1
    if i+z[i] > r: l = i; r = i+z[i]

print(s)
for i in range(1, n):
    print(i, z[i], s[i:], s[:z[i]])