S = 'mississippi'
N = len(S)
i = 0
Z = []
while i < N:
    j = i+1; k = i
    while j < N and S[k] <= S[j]:
        if S[k] < S[j]: k = i
        else: k += 1
        j += 1
    while i <= k: Z += [j-k]; i += j-k

# Z here is the length of the respective strings
print(Z)
p = 0; print([S[p:(p:=p+l)] for l in Z])