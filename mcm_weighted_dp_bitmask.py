from array import *
V = 0; G = [{} for _ in range(V)]; INF = 10**9; P = [1<<i for i in range(V+1)]; I = {1<<i:i for i in range(V+1)}; D = array('i', [-1]*P[V])
def dp(bm):
    if bm == 0: return 0
    if D[bm] != -1: return D[bm]
    nxt = bm&-bm; bm2 = bm^nxt; ans = INF
    while bm2:
        nxt2 = bm2&-bm2
        if I[nxt2] in G[I[nxt]]: ans = min(ans, G[I[nxt]][I[nxt2]]+dp(bm^nxt^nxt2))
        bm2 ^= nxt2
    D[bm] = ans; return ans
print(dp(P[V]-1))