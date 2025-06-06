# https://en.wikipedia.org/wiki/Conjugate_gradient_method#The_resulting_algorithm
# A is a real, symmetric positive-definite matrix, b is also a vector
# Solve Ax = b in O(kn^2) instead of O(n^3), where k is sufficiently small (i.e. k <<< n)
# This should also be the minimizer of f(x) = 0.5*x^T*A*x - x^T*b
EPS = 1e-7
def conjugate_gradient(A, b):
    n = len(b); r = [*b]
    x = [0]*n # initial guess
    for i in range(n):
        for j in range(n): r[i] -= A[i][j]*x[j]
    p = [*r]; Ap = [0]*n
    for _ in range(10): # update the number of iterations here
        rTr = pTAp = new_rTr = 0
        for i in range(n):
            rTr += r[i]*r[i]; Ap[i] = 0
            for j in range(n): Ap[i] += A[i][j]*p[j]
            pTAp += p[i]*Ap[i]
        if pTAp < EPS: break
        alpha = rTr/pTAp
        for i in range(n): x[i] += alpha*p[i]; r[i] -= alpha*Ap[i]; new_rTr += r[i]*r[i]
        if new_rTr < EPS: break
        beta = new_rTr/rTr
        for i in range(n): p[i] *= beta; p[i] += r[i]
    print('Done in', _, 'iterations')
    return x

# Example taken from Wikipedia
if __name__ == '__main__':
    print(conjugate_gradient([[4, 1], [1, 3]], [1, 2]))                                                             # should have x = [1/11, 7/11]
    print(conjugate_gradient([[3, -2], [-2, 4]], [1, 1]))                                                           # should have x = [3/4, 5/8]
    print(conjugate_gradient([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]], [6, 25, -11, 15]))  # should have x = [1, 2, -1, 1]