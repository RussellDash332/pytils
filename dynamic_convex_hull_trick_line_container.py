# General version of convex_hull_trick.py, aka dynamic CHT
# Currently still using O(N) pop and insert but should be fast enough in most cases

INF = 10**18
class LineContainer(list):
    def add(lc, k, m):
        def isect(x, y):
            if y == len(lc): lc[x][2] = INF; return 0
            if lc[x][0] == lc[y][0]: p = INF if lc[x][1] > lc[y][1] else -INF
            else: p = (lc[y][1]-lc[x][1])//(lc[x][0]-lc[y][0])
            lc[x][2] = p; return p >= lc[y][2]
        z = 0; h = len(lc)
        while z < h:
            if k < lc[mi:=(z+h)//2][0]: h = mi
            else: z = mi+1
        lc.insert(z, [k, m, 0]); x = y = z; z += 1
        while isect(y, z): lc.pop(z)
        if x and isect(x:=x-1, y): lc.pop(y); isect(x, y)
        while (y:=x) and lc[x:=x-1][2] >= lc[y][2]: lc.pop(y); isect(x, y)
    def query(lc, x):
        z = 0; h = len(lc)-1
        while z < h:
            if x > lc[mi:=(z+h)//2][2]: z = mi+1
            else: h = mi
        l = lc[z]; return l[0]*x+l[1]

if __name__ == '__main__':
    # Empty
    lc = LineContainer()
    try: lc.query(0)
    except: print('Cannot query if LC is empty') # add your own checks to handle empty

    # Maximize: https://codeforces.com/contest/1083/problem/E
    U = [(6, 2, 4), (1, 6, 2), (2, 4, 3), (5, 3, 8), (7, 1, 2)]; N = len(U)
    U.sort() # the sorting here is due to problem statement, not because of preprocessing for LC
    lc = LineContainer()
    lc.add(0, 0); z = 0; dp = [0]
    for x, y, a in U: z = max(z, lc.query(y)+x*y-a); lc.add(-x, z); dp.append(z)
    print(dp)
    # Naive version for reference
    dp = [0]*(N+1); U = [(0, 0, 0)]+U
    for i in range(1, N+1): dp[i] = max(dp[i-1], U[i][0]*U[i][1]-U[i][2]+max(-U[j][0]*U[i][1]+dp[j] for j in range(i)))
    print(dp)

    # Minimize: https://open.kattis.com/problems/coveredwalkway
    X = [1, 23, 45, 67, 101, 124, 560, 789, 990, 1019]; N = len(X); C = 5000
    z = 0; dp = [0]
    lc = LineContainer()
    for x in X: lc.add(2*x, -x*x-z); z = -lc.query(x)+x*x+C; dp.append(z) # negate everything
    print(dp)
    # Naive version for reference
    dp = [0]*(N+1)
    for i in range(1, N+1): dp[i] = X[i-1]**2+C+min(-2*X[j]*X[i-1]+(dp[j]+X[j]**2) for j in range(i))
    print(dp)

    # Random test
    from random import *
    lc = LineContainer()
    L = 500; create_line = lambda: (randint(-L, L), randint(-L, L))
    U = [create_line() for _ in range(randint(20**4, 30**4))] # add random lines
    for k, m in U: lc.add(k, m) # add to LC
    for _ in range(50):
        x = randint(-10**6, 10**6)
        e = max((k*x+m, k, m) for k, m in U) # expected answer
        z = lc.query(x) # wysiwyg?
        print(f'Querying for max({x}*k+m for k,m in U), expected = ({x})*({e[1]})+({e[2]}) = {e[0]}, output = {z}')
        assert e[0] == z, [e, lc] # sanity check
        L += 30
        for _ in range(100): U.append(create_line()); lc.add(*U[-1]) # add 100 random lines