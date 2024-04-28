from collections import *

# smallest subarray size whose sum is >= K
def sw1(A, K):
    w = deque(); s = 0; ans = len(A)
    for i in range(len(A)):
        w.append(A[i]); s += A[i]
        while w and s-w[0] >= K: s -= w.popleft()
        if s >= K: ans = min(ans, len(w))
    return ans

# smallest subarray size where all numbers in range [1..K] are within
def sw2(A, K):
    w = deque(); h = [0]*(K+1); f = 0; ans = len(A)
    for i in range(len(A)):
        w.append((A[i], i))
        if 1 <= A[i] <= K:
            if h[A[i]] == 0: f += 1
            h[A[i]] += 1
        while f == K:
            ans = min(ans, i-w[0][1]+1); v = w.popleft()[0]
            if 1 <= v <= K:
                h[v] -= 1
                if h[v] == 0: f -= 1
    return ans

# max(sum(A[i:i+K]) for i in range(len(A)-K+1))
def sw3(A, K):
    w = deque(); ans = 0; s = 0
    for i in range(len(A)):
        w.append(A[i]); s += A[i]
        if len(w) > K: s -= w.popleft()
        if len(w) == K: ans = max(ans, s)
    return ans

# [min(A[i:i+K]) for i in range(len(A)-K+1)]
def sw4(A, K):
    w = deque(); ans = []
    for i in range(len(A)):
        while w and w[-1][0] >= A[i]: w.pop()
        w.append((A[i], i))
        while w[0][1] <= i-K: w.popleft()
        if i+1 >= K: ans.append(w[0][0])
    return ans

if __name__ == '__main__':
    print(sw1([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15)) # 2
    print(sw1([1, 2, 3, 4, 5], 11)) # 3
    print(sw2([1, 2, 3, 7, 1, 12, 9, 11, 9, 6, 3, 7, 5, 4, 5, 3, 1, 10, 3, 3], 4)) # 13
    print(sw2([1, 2, 3, 7, 1, 12, 9, 11, 9, 6, 3, 7, 5, 4, 5, 3, 1, 10, 3, 3], 3)) # 3
    print(sw3([10, 50, 30, 20, 5, 1], 3)) # 100
    print(sw3([49, 70, 48, 61, 60, 60], 2)) # 121
    print(sw4([0, 5, 5, 3, 10, 0, 4], 3)) # [0, 3, 3, 0, 0]