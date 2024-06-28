def LPCS(s1):
    n = len(s1)

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    sol = [[0, 0] * (n + 1) for _ in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][i] = 1

    """for i in range(n):
        dp[i + 1][i] = 0"""
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = l + i - 1
            if s1[i] == s1[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
                sol[i][j] = [-1, -1]
            else:
                if dp[i + 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i + 1][j]
                    sol[i][j] = [0, -1]
                else:
                    dp[i][j] = dp[i][j - 1]
                    sol[i][j] = [-1, 0]

    return dp[0][n - 1], sol

def printSol(sol, s1, i, j):
    if i > j:
        return ""
    if i == j:
        return s1[i]
    if sol[i][j] == [-1, -1]:
        return s1[i] + printSol(sol, s1, i + 1, j - 1) + s1[j]
    elif sol[i][j] == [0, -1]:
        return printSol(sol, s1, i + 1, j)
    else:
        return printSol(sol, s1, i, j - 1)

s1 = "ABBDCACB"
n = len(s1)

maxLenght, solutionArr = LPCS(s1)

print(maxLenght)
result = printSol(solutionArr, s1, 0, n - 1)
print(result)