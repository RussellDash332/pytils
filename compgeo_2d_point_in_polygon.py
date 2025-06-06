# Represent a point as a tuple of (x, y)
# Represent a polygon as a list of points
def pip(p, P):
    z = False; n = len(P)
    for i in range(n):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%n][0]-p[0], P[(i+1)%n][1]-p[1])
        if a[1] > b[1]: a, b = b, a
        if a[1] <= 0 and b[1] > 0 and a[0]*b[1] < a[1]*b[0]: z = not z
        if a[0]*b[1] == a[1]*b[0] and a[0]*b[0]+a[1]*b[1] <= 0: return True
    return z

if __name__ == '__main__':
    shape = [(1, 1), (3, 3), (9, 1), (12, 4), (9, 7), (1, 7)]
    shape.append(shape[0])
    print(pip((3, 2), shape))
    print(pip((3, 3), shape))
    print(pip((5, 7), shape))
    print(pip((3, 4), shape))
    print(pip((8, -4), shape))
    print(shape)