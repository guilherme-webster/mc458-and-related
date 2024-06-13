def stackTiles(h, m, k):
    dp = [[0 for j in range(m + 2)]  
             for i in range(h + 1)]
    presum = [0] * (m + 1)

    for j in range(m + 2):
        dp[0][j] = 1
    presum[0] = 1 

    for i in range(1, h + 1):
        dp[i][m + 1] = 0

    for j in range(m, 0, -1):
        for i in range(1, h + 1):
            for x in range(k + 1):
               dp[i][j] += dp[i - x][j + 1]

    return dp[h][1]

# Driver Code 
h, m, k = 3, 3, 2
  
print(stackTiles(h, m, k))