def knapsack(capacity, vals, weights):
    n = len(vals)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if j >= weights[i-1]: dp[i][j] = max(dp[i-1][j-weights[i-1]]+vals[i-1], dp[i-1][j])
            else: dp[i][j] = dp[i-1][j]
    return dp