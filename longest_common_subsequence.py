def lcs(A, B):
    N = len(A)+1; M = len(B)+1; dp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0: dp[i][j] = 0
            elif A[i-1] == B[j-1]: dp[i][j] = dp[i-1][j-1]+1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # return dp[N][M] here if you don't need to reconstruct
    i = N-1; j = M-1; z = []; T = z.append
    while i and j:
        if A[i-1] == B[j-1]: T(A[i-1]); i -= 1 ; j -= 1
        elif dp[i-1][j] >= dp[i][j-1]: i -= 1
        else: j -= 1
    return z[::-1]

# LCS of two permutations reduces to LIS
from bisect import *
def lis(A):
    B = []
    for e in A:
        p = bisect(B, e-1)
        if p == len(B): B.append(e)
        else: B[p] = e
    return B
def lcs_perm(p1, p2):
    c = []; r = {e:i for i,e in enumerate(p1)}
    for i in p2: c.append(r[i])
    return [p1[i] for i in lis(c)]

if __name__ == '__main__':
    a = 'education'
    b = 'teacher'
    print(lcs(a, b))

    a = [0, 1, 2, 3, 4, 5]
    b = [4, 3, 2, 2, 3, 5]
    print(lcs(a, b))

    a = [1, 5, 4, 8, 3, 9]
    b = [1, 4, 3, 5, 8, 9]
    print(lcs_perm(a, b))