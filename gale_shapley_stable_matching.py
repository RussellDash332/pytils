def gale_shapley(M, F):
    n = len(M); m = len(F); pos = [0]*n; r = [{e:i for i,e in enumerate(_)} for _ in F]; Z = {}; S = {*range(n)}
    while S:
        a = S.pop()
        if pos[a] == m: return None
        b = M[a][pos[a]]; pos[a] += 1
        if b not in Z: Z[b] = a
        elif r[b][c:=Z[b]] < r[b][a]: S.add(a)
        else: S.add(c); Z[b] = a
    return [(a, b) for b, a in Z.items()]

# 1a, 2d, 3b, 4c
M = [[0, 2, 1, 3], [3, 2, 1, 0], [1, 0, 3, 2], [2, 3, 0, 1]] # jobs 1-4, e.g. job 3 prefers applicant b-a-d-c
F = [[2, 3, 1, 0], [0, 3, 1, 2], [1, 2, 0, 3], [2, 0, 1, 3]] # applicants a-d, e.g. applicant b prefers 1-4-2-3
print(gale_shapley(M, F))

# https://open.kattis.com/problems/jealousyoungsters, sample 1
M = [[0, 2, 1], [1, 0, 2]]
F = [[0, 1], [1, 0], [0, 1]]
print(gale_shapley(M, F))

# https://open.kattis.com/problems/jealousyoungsters, sample 2
M = [[0], [0]]
F = [[0, 1]]
print(gale_shapley(M, F))