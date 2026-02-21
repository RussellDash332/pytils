A = [564, 7167, -4069, -3244, 579, 199, -9838, 2913, 9796, 4734]
N = len(A)
K = len(bin(N))-1


# Range sum query
S = [[*A]]; B = 1
for i in range(1, K+1): S.append([S[-1][j]+S[-1][j+B] for j in range(N+1-2*B)]); B <<= 1
def query(l, r):
    s = 0
    for i in range(K, -1, -1):
        if 1<<i <= r-l: s += S[i][l]; l += 1<<i
    return s

if __name__ == '__main__':
    for r in range(N+1):
        for l in range(r+1): assert query(l, r) == sum(A[l:r]), [(l, r), (query(l, r), sum(A[l:r]))]


# Range min/max query
# for range min query, change all max to min
S = [[*A]]; B = 1
D = -max(-10**18, 10**18)
for i in range(1, K+1): S.append([max(S[-1][j], S[-1][j+B]) for j in range(N+1-2*B)]); B <<= 1
def query(l, r):
    if l >= r: return D
    return max(S[i:=(r-l).bit_length()-1][l], S[i][r-(1<<i)])

if __name__ == '__main__':
    for r in range(N+1):
        for l in range(N+1): assert query(l, r) == max(A[l:r], default=D), [(l, r), (query(l, r), max(A[l:r], default=D))]