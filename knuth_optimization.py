# Knuth's Optimization
# The general version of the (sorted) convex hull trick
# Optimize dp[i] = min(dp[j]+f(i,j) for j in range(i)) from O(N^2) to O(N log N)

# Change to >= for maximization
def turn(j, k):
    l = 1; r = N+1
    while l < r:
        if f(m:=(l+r)//2,k) <= f(m,j): r = m
        else: l = m+1
    return l

# Minimize: https://open.kattis.com/problems/coveredwalkway
def f(i, j): return dp[j] + (P[i]-P[j+1])**2 + C
from collections import *
P = [1, 23, 45, 67, 101, 124, 560, 789, 990, 1019]; N = len(P); P = [0]+P; C = 5000; dp = [0]; Q = deque([0])
for i in range(1, N+1):
    while len(Q) > 1 and turn(Q[0], Q[1]) <= i: Q.popleft()
    dp.append(f(i, Q[0]))
    if i == N: break
    while len(Q) > 1 and turn(Q[-2], Q[-1]) >= turn(Q[-1], i): Q.pop()
    Q.append(i)
print(dp)

# Also minimize: https://open.kattis.com/problems/marathon2
def f(i, j): d = P[i]-P[j]; u = min(d, X); return dp[j] + u*S + (d-u)*H + Y*H*S
from collections import *
P = [100, 800, 1200, 20000, 30000, 42195]; N = len(P); P = [0]+P; X = 500; Y = 20; H = 8; S = 3; dp = [0]; Q = deque([0])
for i in range(1, N+1):
    while len(Q) > 1 and turn(Q[0], Q[1]) <= i: Q.popleft()
    dp.append(f(i, Q[0]))
    if i == N: break
    while len(Q) > 1 and turn(Q[-2], Q[-1]) >= turn(Q[-1], i): Q.pop()
    Q.append(i)
print([i-Y*H*S for i in dp])