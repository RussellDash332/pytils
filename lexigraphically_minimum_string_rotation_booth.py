def booth(s):
    n = len(s); f = [-1]*2*n; k = 0
    for j in range(1, 2*n):
        i = f[j-k-1]
        while i != -1 and s[j % n] != s[(k+i+1)%n]:
            if s[j%n] < s[(k+i+1)%n]: k = j-i-1
            i = f[i]
        if i == -1 and s[j%n] != s[(k+i+1)%n]:
            if s[j%n] < s[(k+i+1)%n]: k = j
            f[j-k] = -1
        else: f[j-k] = i+1
    return s[k:]+s[:k]

s = 'DEFBCA'
print(s, booth(s))

s = 'ZAAAAAA'
print(s, booth(s))