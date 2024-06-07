# Assumption: px and py are list of complex numbers, px sorted by x, py sorted by y
def closest_pair(px, py):
    if len(px) < 40: # just brute-force it
        d = 1e9
        for i in range(len(px)-1):
            for j in range(i+1, len(px)):
                if (d2:=abs(px[i]-px[j])) < d: d, p1, p2 = d2, px[i], px[j]
        return d, p1, p2
    mid = len(px)//2; xmid = px[mid].real; py1, py2 = [], []
    for i in py:
        if i.real < xmid: py1.append(i)
        else: py2.append(i)
    d, p1, p2 = min(closest_pair(px[:mid], py1), closest_pair(px[mid:], py2)); q = [i for i in py if abs(i.real-xmid) < d]
    for i in range(len(q)-1):
        for j in range(i+1, min(i+7, len(q))):
            if (d2:=abs(q[i]-q[j])) < d: d, p1, p2 = d2, q[i], q[j]
            else: break
    return d, p1, p2