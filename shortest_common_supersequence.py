def scs(A, B):
    N = len(A)+1; M = len(B)+1; dp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0: dp[i][j] = j
            elif j == 0: dp[i][j] = i
            elif A[i-1] == B[j-1]: dp[i][j] = dp[i-1][j-1]+1
            else: dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
    # return dp[N][M] here if you don't need to reconstruct
    i = N-1; j = M-1; z = []; T = z.append
    while i and j:
        if A[i-1] == B[j-1]: T(A[i-1]); i -= 1 ; j -= 1
        elif dp[i-1][j] > dp[i][j-1]: T(B[j-1]); j -= 1
        else: T(A[i-1]); i -= 1
    while i: T(A[i-1]); i -= 1
    while j: T(B[j-1]); j -= 1
    return z[::-1]

if __name__ == '__main__':
    a = 'education'
    b = 'teacher'
    print(scs(a, b))

    a = [0, 1, 2, 3, 4, 5]
    b = [4, 3, 2, 2, 3, 5]
    print(scs(a, b))