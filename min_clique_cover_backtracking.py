# Minimum clique cover
def bt(cl, v, z):
    if v < n:
        for i in range(1, v+2):
            cl[v] = i; d[i].append(v); ok = 1
            for j in range(len(d[i])-1):
                if am[d[i][j]][v] < 1: ok = 0; break
            if ok and max(cl) < z: z = bt(cl, v+1, z)
            cl[v] = 0; d[i].pop()
    elif (m:=max(cl)) < z: z = m
    return z

def bt_show_clique(cl, v, z):
    if v < n:
        for i in range(1, v+2):
            cl[v] = i; d[i].append(v); ok = 1
            for j in range(len(d[i])-1):
                if am[d[i][j]][v] < 1: ok = 0; break
            if ok and max(cl) < z[0]: z = bt_show_clique(cl, v+1, z)
            cl[v] = 0; d[i].pop()
    elif (m:=max(cl)) < z[0]: z = (m, [*cl])
    return z

if __name__ == '__main__':
    am = [
        [1, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]

    # Initial assignment of cliques - 0 means unassigned
    n = len(am)
    d = {i:[] for i in range(1, n+1)}; d[1].append(0)
    cl = [1]+[0]*(n-1)
    print(bt(cl, 1, n+1))

    # If you need the cliques
    n = len(am)
    d = {i:[] for i in range(1, n+1)}; d[1].append(0)
    cl = [1]+[0]*(n-1)
    print(bt_show_clique(cl, 1, (n+1, None)))