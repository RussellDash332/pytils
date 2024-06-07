# Chinese Postman Problem
# In this graph, g[i][j] is a list of numbers and not single-valued
INF = float('inf')

def fw(g, v):
    D = [[min(g[i][j]) if i in g and j in g[i] else INF for j in range(v)] for i in range(v)]
    for k in range(v):
        for i in range(v):
            for j in range(v): D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

# https://stackoverflow.com/questions/5360220/how-to-split-a-list-into-pairs-in-all-possible-ways
def all_pairs(lst):
    if len(lst) < 2: yield []; return
    if len(lst) % 2:
        for i in range(len(lst)):
            for result in all_pairs(lst[:i] + lst[i+1:]): yield result
    else:
        for i in range(1, len(lst)):
            pair = (lst[0], lst[i])
            for rest in all_pairs(lst[1:i] + lst[i+1:]): yield [pair] + rest

# degree pre-calculated
def cpp(g, deg):
    D = fw(g, len(deg)); e = 0; odd = [i for i in range(len(deg)) if deg[i] % 2]; add = INF
    for pairings in all_pairs(odd): add = min(add, sum(D[i][j] for i, j in pairings))
    for i in g:
        for j in g[i]: e += sum(g[i][j])
    return e // 2 + add