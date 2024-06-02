a = [2, 3, 1, 5, 7, -1, -2, 3, 4, 4, 3]
z = [None]*len(a); s = []
for i in range(len(a)):
    while s and s[-1][1] < a[i]: z[s.pop()[0]] = a[i]
    s.append((i, a[i]))
print(a); print(z)