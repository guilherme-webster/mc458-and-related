def knapsackDP(v, w, n, W):

    dp = [[0] * (W + 1) for _ in range(n + 1)]
    sol = [0] * (n)

    # Base cases
    """for i in range(n + 1):
        dp[i][0] = 0

    for j in range(W + 1):
        dp[0][j] = 0"""
        
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j]
            if w[i - 1] <= j and dp[i - 1][j - w[i - 1]] + v[i - 1] > dp[i][j]:
                dp[i][j] = dp[i - 1][j - w[i - 1]] + v[i - 1]
                sol[i - 1] = 1

    return dp[n][W], sol

v = [1, 2, 1, 6]
w = [1, 3, 4, 2]
W = 6

maxValue, solution = knapsackDP(v, w, 4, W)

print(maxValue)
print(solution)