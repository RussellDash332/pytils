M = 10**9+7
M2 = 10**9-63
P = 31
P2 = 67

S = 'abchelloworldabcfantasticabc'
N = len(S)
F = [f:=1]+[f:=f*P%M for _ in range(N)]
F2 = [f:=1]+[f:=f*P2%M2 for _ in range(N)]


# single modulo hash
def get(l, r): # S[l:r]
    return (H[r]-H[l]*F[r-l])%M
def replace(l, r, x, c): # S[l:x]+c+S[x+1:r] where c is a single character
    return (get(l, x)*F[r-x]+ord(c)*F[r-x-1]+get(x+1, r))%M
H = [0]
for i in range(N): p = H[-1]; c = ord(S[i]); H.append((p*P+c)%M)

if __name__ == '__main__':
    print(get(0, 1), get(17, 18), get(25, 26))
    print(get(0, 3), get(13, 16))
    print(get(5, 5))
    print(get(3, 13), replace(3, 13, 8, 'w'), replace(3, 13, 12, 'e')) # helloworld, helloworld, helloworle


# double modulo hash
def get(l, r): # S[l:r]
    return (H[r][0]-H[l][0]*F[r-l])%M, (H[r][1]-H[l][1]*F2[r-l])%M2
def replace(l, r, x, c): # S[l:x]+c+S[x+1:r] where c is a single character
    a, b = get(l, x); p, q = get(x+1, r)
    return (a*F[r-x]+ord(c)*F[r-x-1]+p)%M, (b*F2[r-x]+ord(c)*F2[r-x-1]+q)%M2
H = [(0, 0)]
for i in range(N): p, p2 = H[-1]; c = ord(S[i]); H.append(((p*P+c)%M, (p2*P2+c)%M2))

if __name__ == '__main__':
    print(get(0, 1), get(17, 18), get(25, 26))
    print(get(0, 3), get(13, 16))
    print(get(5, 5))
    print(get(3, 13), replace(3, 13, 8, 'w'), replace(3, 13, 12, 'e')) # helloworld, helloworld, helloworle


# oop version
class Hash:
    def __init__(self, s):
        self.h1 = [0]; self.h2 = [0]
        for i in range(N): c = ord(S[i]); self.h1.append((self.h1[-1]*P+c)%M); self.h2.append((self.h2[-1]*P2+c)%M2)
    def get(self, l, r):
        return (self.h1[r]-self.h1[l]*F[r-l])%M, (self.h2[r]-self.h2[l]*F2[r-l])%M2
    def replace(self, l, r, x, c):
        a, b = self.get(l, x); p, q = self.get(x+1, r)
        return (a*F[r-x]+ord(c)*F[r-x-1]+p)%M, (b*F2[r-x]+ord(c)*F2[r-x-1]+q)%M2

if __name__ == '__main__':
    H = Hash(S)
    print(H.get(0, 1), H.get(17, 18), H.get(25, 26))
    print(H.get(0, 3), H.get(13, 16))
    print(H.get(5, 5))
    print(H.get(3, 13), H.replace(3, 13, 8, 'w'), H.replace(3, 13, 12, 'e')) # helloworld, helloworld, helloworle