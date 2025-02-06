# Represent a point as a tuple of (x, y)
# Represent a polygon as a list of points

# Assumes {*chull(p)} == {*p}
def area(p):
    a, n = 0, len(p)
    for i in range(n): a += p[i][0]*p[(i+1)%n][1]-p[i][1]*p[(i+1)%n][0]
    return abs(a)/2

def centroid(p):
    a = cx = cy = 0; n = len(p)
    for i in range(n): d = p[i][0]*p[(i+1)%n][1]-p[(i+1)%n][0]*p[i][1]; a += d; cx += (p[i][0]+p[(i+1)%n][0])*d; cy += (p[i][1]+p[(i+1)%n][1])*d
    return (cx/a/3, cy/a/3)

if __name__ == '__main__':
    shape = [(1, 1), (3, 3), (9, 1), (12, 4), (9, 7), (1, 7)]
    shape.append(shape[0])
    print(area(shape))
    print(centroid(shape))