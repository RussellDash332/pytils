def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]

def minkowski(P, Q):
    p = P.index(min(P)); q = Q.index(min(Q)); a = len(P); b = len(Q); R = [(P[p][0]+Q[q][0], P[p][1]+Q[q][1])]; i = p; j = q
    while i < p+a or j < q+b:
        if i == p+a: j += 1
        elif j == q+b: i += 1
        else:
            if (c:=(P[(i+1)%a][0]-P[i%a][0])*(Q[(j+1)%b][1]-Q[j%b][1])-(P[(i+1)%a][1]-P[i%a][1])*(Q[(j+1)%b][0]-Q[j%b][0])) >= 0: i += 1
            if c <= 0: j += 1
        R.append((P[i%a][0]+Q[j%b][0], P[i%a][1]+Q[j%b][1]))
    return R

if __name__ == '__main__':
    P = [(1, 1), (1, 2), (0, 2), (0, 1)]
    Q = [(2, 2), (1, 2), (2, 1)]
    print(minkowski(P, Q))

    P = [(2, 1), (4, 1), (4, 3), (2, 3)]
    Q = [(-3, 1), (-2, 2), (-4, 2)]
    print(minkowski(P, Q))