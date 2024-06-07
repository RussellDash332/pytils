V = 7
g = [[] for _ in range(V)]

V = 7
g = [[1, 6], [2], [3, 4], [0], [5], [0, 2], [5]] # CP4 example graph

source = 0
ans, idx, stack = [], [0]*V, [source]
while stack:
    u = stack[-1]
    if idx[u] < len(g[u]):  stack.append(g[u][idx[u]]); idx[u] += 1
    else:                   ans.append(u), stack.pop()
ans = ans[::-1]

print(*ans)