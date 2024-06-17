# CHT to solve the DP relation in O(N) instead of O(N^2)
# dp[i] = max/min(dp[i-1], c[i]+max/min(a[j]*x[i]+b[j] for j in range(i)))

# Maximize: https://codeforces.com/contest/1083/problem/E
from collections import *
def ccw(p, q, r):
    return (r[1]-q[1])*(p[0]-q[0]) >= (q[0]-r[0])*(q[1]-p[1])
L = [(6, 2, 4), (1, 6, 2), (2, 4, 3), (5, 3, 8), (7, 1, 2)]; N = len(L)
L.sort(); Q = deque([(0, 0)]); z = 0; dp = [0]
for x, y, a in L:
    while len(Q) > 1 and (Q[0][0]-Q[1][0])*y <= Q[1][1]-Q[0][1]: Q.popleft()
    z = max(z, Q[0][0]*y+Q[0][1]+x*y-a); new = (-x, z)
    while len(Q) > 1 and ccw(Q[-2], Q[-1], new): Q.pop()
    Q.append(new); dp.append(z)
print(dp)
# Naive version for reference
dp = [0]*(N+1); L = [(0, 0, 0)]+L
for i in range(1, N+1): dp[i] = max(dp[i-1], L[i][0]*L[i][1]-L[i][2]+max(-L[j][0]*L[i][1]+dp[j] for j in range(i)))
print(dp)

# Minimize: https://open.kattis.com/problems/coveredwalkway
from collections import *
def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) >= (r[0]-p[0])*(q[1]-p[1])
X = [1, 23, 45, 67, 101, 124, 560, 789, 990, 1019]; N = len(X); C = 5000
Q = deque(); z = 0; dp = [0]
for x in X:
    new = (-2*x, x*x+z)
    while len(Q) > 1 and ccw(Q[-2], Q[-1], new): Q.pop()
    Q.append(new)
    while len(Q) > 1 and (Q[0][0]-Q[1][0])*x >= Q[1][1]-Q[0][1]: Q.popleft()
    z = Q[0][0]*x+Q[0][1]+x*x+C; dp.append(z)
print(dp)
# Naive version for reference
dp = [0]*(N+1)
for i in range(1, N+1): dp[i] = X[i-1]**2+C+min(-2*X[j]*X[i-1]+(dp[j]+X[j]**2) for j in range(i))
print(dp)